#include "../src/main.cpp"
#include <cstdio>
static float frame_mA(){ float s=0; for(auto c:led.px) s+=((c>>16)&255)+((c>>8)&255)+(c&255); return s/255.f*20.f + COUNT*1.f; }
static void run(uint32_t ms){ for(uint32_t i=0;i<ms;i++){ g_ms++; loop(); } }
static void click(int pin,uint32_t hold){ g_pin[pin]=LOW; run(hold); g_pin[pin]=HIGH; run(60); }
int main(){ for(int i=0;i<64;i++) g_pin[i]=HIGH; g_ms=1000; setup();
  const char* nm[]={"BREATH","CHARGE","CHASE","SURGE","FLASH","SPARK"}; int ok=1;
  level=3; float worst=0;
  for(int e=0;e<5;e++){ float mx=0; for(int k=0;k<4000;k++){ run(1); float m=frame_mA(); if(m>mx)mx=m; } printf("%-6s effect=%d peak est %.0f mA\n", nm[effect], effect, mx); if(mx>worst)worst=mx; if(effect==FLASH) ok=0; click(MODE_PIN,100); run(500); }
  printf("cycle returned to %s\n", nm[effect]); if(effect!=BREATH) ok=0;
  click(MODE_PIN,100); run(500); Effect before=effect;                      // CHARGE
  click(ACTION_PIN,80); run(40); click(ACTION_PIN,80);                      // double -> flash
  float mx=0; int sawFlash=0; for(int k=0;k<300;k++){ run(1); if(effect==FLASH) sawFlash=1; float m=frame_mA(); if(m>mx)mx=m; }
  run(400); printf("flash seen=%d peak est %.0f mA, resumed %s (expected %s)\n", sawFlash, mx, nm[effect], nm[before]); if(!sawFlash||effect!=before) ok=0; if(mx>worst)worst=mx;
  uint8_t lv=level; click(ACTION_PIN,100); run(500); printf("B short: level %d -> %d\n", lv, level); if(level==lv) ok=0;
  uint8_t pal=palette; click(ACTION_PIN,1000); run(100); printf("B long: palette %d -> %d\n", pal, palette); if(palette==pal) ok=0;
  click(MODE_PIN,1000); run(100); printf("A long: on=%d\n", on); if(on) ok=0; run(100); if(frame_mA()>COUNT*1.f+0.5f) ok=0;
  click(MODE_PIN,1000); run(100); if(!on) ok=0;
  g_ms=0xFFFFFF00u; frameAt=g_ms; effectAt=g_ms; int s0=led.shows; run(600); printf("frames across millis rollover: %d\n", led.shows-s0); if(led.shows-s0<20) ok=0;
  printf("COUNT=%d LIMIT_MA=%d worst est %.0f mA -> %s\n", COUNT, LIMIT_MA, worst, (ok && worst<=LIMIT_MA+1)?"PASS":"FAIL"); return !(ok && worst<=LIMIT_MA+1); }
