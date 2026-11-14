// Standalone ESP32 reference firmware for the Vi gauntlet lighting. NOT WLED.
// Original draft: ChatGPT (2026-11-14). Revised by Claude (2026-11-14) after code review:
//   F1 Button struct now has a constructor (builds as C++11).
//   F2 Software current limiter: frame is scaled down if its estimated draw exceeds LIMIT_MA.
//   F3 Pixel layout selectable at build time; chase speed/tail scale with the pixel count.
//   F4 Periodic effects use (t % period), so they stay smooth after hours of run time.
//   F5 Pins overridable from platformio.ini build flags.
// STATUS: syntax-checked on a PC against stub headers only. NOT built for ESP32, NOT flashed,
// NOT bench tested. The limiter is an estimate, not a fuse: keep the 3 A inline fuse.
//
// Wiring (reference DevKit): LED_PIN -> 5 V level shifter -> 330R -> ring DIN -> hand -> crystal.
// MODE_PIN / ACTION_PIN: momentary normally-open switches to GND (internal pull-ups).
#include <Arduino.h>
#include <Adafruit_NeoPixel.h>
#include <math.h>
#include <string.h>

#ifndef LED_PIN
#define LED_PIN 16
#endif
#ifndef MODE_PIN
#define MODE_PIN 25
#endif
#ifndef ACTION_PIN
#define ACTION_PIN 26
#endif
#ifndef LIMIT_MA
#define LIMIT_MA 1000            // estimated LED current ceiling per arm
#endif

// Layout: default = 144 LEDs/m strip (ring 50, hand 34, crystal 9).
// Build with -DLAYOUT_60 for the 60 LEDs/m layout (21 / 14 / 4), -DRING_ONLY to drive the ring alone.
#ifdef LAYOUT_60
constexpr int RING = 21, HAND_FULL = 14, CRYSTAL_FULL = 4;
#else
constexpr int RING = 50, HAND_FULL = 34, CRYSTAL_FULL = 9;
#endif
#ifdef RING_ONLY
constexpr int HAND = 0, CRYSTAL = 0;
#else
constexpr int HAND = HAND_FULL, CRYSTAL = CRYSTAL_FULL;
#endif
constexpr int COUNT = RING + HAND + CRYSTAL;

constexpr uint32_t FRAME_MS = 25, DEBOUNCE_MS = 35, LONG_MS = 850, DOUBLE_MS = 360, FLASH_MS = 350;
constexpr uint32_t BREATH_MS = 2244, CHARGE_MS = 2600, RING_REV_MS = 1400, HAND_RUN_MS = 1300,
                   CRYSTAL_MS = 700, SURGE_MS = 1650;
constexpr float MA_PER_CHANNEL = 20.0f, MA_IDLE_PER_PIXEL = 1.0f;   // planning figures, not measured
const uint8_t BRIGHT[] = {32, 64, 96, 128};                          // user brightness steps (of 255)
constexpr float TWO_PI_F = 6.2831853f;

Adafruit_NeoPixel led(COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
enum Effect : uint8_t { BREATH, CHARGE, CHASE, SURGE, FLASH, SPARK };
Effect effect = BREATH, resumeEffect = BREATH;
bool on = true;
uint8_t level = 1, palette = 0;
uint8_t spark[COUNT] = {};
uint8_t frame[COUNT][3];
uint32_t effectAt = 0, flashAt = 0, frameAt = 0;

struct Button {
  int pin; bool raw, stable, longDone; uint8_t clicks; uint32_t changed, pressed, released;
  explicit Button(int p) : pin(p), raw(false), stable(false), longDone(false), clicks(0),
                           changed(0), pressed(0), released(0) {}
};
Button a(MODE_PIN), b(ACTION_PIN);

static uint8_t u8(float x) { return x < 0 ? 0 : x > 255 ? 255 : uint8_t(x + 0.5f); }
static float phase(uint32_t t, uint32_t period) { return (t % period) / float(period); }   // 0..1

void baseColor(uint8_t &r, uint8_t &g, uint8_t &bl) {
  if (palette == 0) { r = 0; g = 120; bl = 255; }          // hextech blue
  else if (palette == 1) { r = 130; g = 20; bl = 255; }    // violet
  else { r = 230; g = 30; bl = 190; }                      // magenta
}
void put(int i, float r, float g, float bl, float intensity) {
  if (i < 0 || i >= COUNT) return;
  if (intensity < 0) intensity = 0;
  float f = BRIGHT[level] / 255.0f * intensity;
  frame[i][0] = u8(r * f); frame[i][1] = u8(g * f); frame[i][2] = u8(bl * f);
}
// Estimate current for the frame and scale it down to stay under LIMIT_MA, then send it.
void showLimited() {
  uint32_t sum = 0;
  for (int i = 0; i < COUNT; i++) sum += frame[i][0] + frame[i][1] + frame[i][2];
  float idle = COUNT * MA_IDLE_PER_PIXEL;
  float lit = sum / 255.0f * MA_PER_CHANNEL;
  float budget = float(LIMIT_MA) - idle;
  float k = (budget > 0 && lit > budget) ? budget / lit : (budget > 0 ? 1.0f : 0.0f);
  for (int i = 0; i < COUNT; i++)
    led.setPixelColor(i, led.Color(uint8_t(frame[i][0] * k), uint8_t(frame[i][1] * k), uint8_t(frame[i][2] * k)));  // truncate: never round above the limit
  led.show();
}
void setEffect(Effect e) { effect = e; effectAt = millis(); if (e == SPARK) memset(spark, 0, sizeof(spark)); }

void shortPress(bool mode) {
  if (mode) {                                   // A short: next effect (FLASH is never in the cycle)
    if (effect == FLASH) effect = resumeEffect;
    Effect next = (effect == SPARK) ? BREATH : Effect(uint8_t(effect) + 1);
    if (next == FLASH) next = SPARK;
    setEffect(next);
  } else level = (level + 1) % (sizeof(BRIGHT) / sizeof(BRIGHT[0]));   // B short: brightness step
}
void longPress(bool mode) { if (mode) on = !on; else palette = (palette + 1) % 3; }
void doublePress(bool mode) {
  if (mode) { shortPress(true); return; }
  if (effect != FLASH) resumeEffect = effect;   // B double: one-shot flash, then resume
  effect = FLASH; flashAt = millis();
}
void poll(Button &x, bool isMode, uint32_t now) {
  bool raw = digitalRead(x.pin) == LOW;
  if (raw != x.raw) { x.raw = raw; x.changed = now; }
  if (raw != x.stable && now - x.changed >= DEBOUNCE_MS) {
    x.stable = raw;
    if (raw) { x.pressed = now; x.longDone = false; }
    else if (!x.longDone) { x.clicks++; x.released = now; if (x.clicks >= 2) { x.clicks = 0; doublePress(isMode); } }
  }
  if (x.stable && !x.longDone && now - x.pressed >= LONG_MS) { x.longDone = true; x.clicks = 0; longPress(isMode); }
  if (!x.stable && x.clicks == 1 && now - x.released >= DOUBLE_MS) { x.clicks = 0; shortPress(isMode); }
}
// Comet: bright head with a fading tail, wrapping around n pixels starting at 'first'.
void comet(int first, int n, uint32_t t, uint32_t periodMs, float peak, uint8_t r, uint8_t g, uint8_t bl) {
  if (n <= 0) return;
  int tail = n / 4; if (tail < 3) tail = 3;
  int head = int(phase(t, periodMs) * n) % n;
  for (int i = 0; i < n; i++) {
    int d = (head - i + n) % n;
    put(first + i, r, g, bl, d < tail ? peak * (1.0f - d / float(tail)) : 0.02f);
  }
}
void draw(uint32_t now) {
  memset(frame, 0, sizeof(frame));
  if (!on) { showLimited(); return; }
  if (effect == FLASH && now - flashAt >= FLASH_MS) setEffect(resumeEffect);
  uint8_t r, g, bl; baseColor(r, g, bl);
  uint32_t t = now - effectAt;
  const int H0 = RING, C0 = RING + HAND;
  if (effect == BREATH) {
    float v = 0.30f + 0.24f * sinf(TWO_PI_F * phase(t, BREATH_MS));
    for (int i = 0; i < COUNT; i++) put(i, r, g, bl, v * (i >= C0 ? 1.3f : i >= H0 ? 0.65f : 1.0f));
  } else if (effect == CHARGE) {
    float v = phase(t, CHARGE_MS);
    for (int i = 0; i < RING; i++) put(i, r, g, bl, i / float(RING) < v ? 0.95f : 0.02f);
    for (int i = 0; i < HAND; i++) put(H0 + i, r, g, bl, i / float(HAND) < v ? 0.65f : 0.02f);
    for (int i = C0; i < COUNT; i++) put(i, r, g, bl, v > 0.84f ? 1.0f : v * 0.3f);
  } else if (effect == CHASE) {
    comet(0, RING, t, RING_REV_MS, 1.0f, r, g, bl);
    comet(H0, HAND, t, HAND_RUN_MS, 0.8f, r, g, bl);
    for (int i = C0; i < COUNT; i++) put(i, r, g, bl, 0.25f + 0.2f * sinf(TWO_PI_F * phase(t, CRYSTAL_MS)));
  } else if (effect == SURGE) {
    uint32_t p = t % SURGE_MS; float v = p < 190 ? 1.0f - p / 250.0f : 0.11f;
    for (int i = 0; i < COUNT; i++) put(i, r, g, bl, v);
  } else if (effect == FLASH) {
    float v = (now - flashAt) % 95UL < 50UL ? 1.0f : 0.12f;
    for (int i = 0; i < COUNT; i++) put(i, 185, 220, 255, v);
  } else if (effect == SPARK) {
    for (int i = 0; i < COUNT; i++) { spark[i] = uint8_t(spark[i] * 0.77f); put(i, r, g, bl, 0.07f + spark[i] / 255.0f); }
    int n = COUNT / 20; if (n < 2) n = 2;                    // keep spark density similar on longer strips
    for (int k = 0; k < n; k++) spark[random(COUNT)] = (k & 1) ? 185 : 255;
  }
  showLimited();
}
void setup() {
  pinMode(MODE_PIN, INPUT_PULLUP); pinMode(ACTION_PIN, INPUT_PULLUP);
  led.begin(); led.clear(); led.show();
  randomSeed(esp_random()); effectAt = millis();
}
void loop() {
  uint32_t now = millis();
  poll(a, true, now); poll(b, false, now);
  if (now - frameAt >= FRAME_MS) { frameAt = now; draw(now); }
}
