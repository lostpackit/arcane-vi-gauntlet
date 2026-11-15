# Standalone Arduino firmware — alternative to WLED

WLED is the preferred path. This sketch is the fallback that gives the exact button behaviour, including a 350 ms flash that returns to the previous effect.

**Status (2026-11-14, Claude revision of the ChatGPT draft):** compiles cleanly with `g++ -Wall -Wextra` as gnu++11 and gnu++17 against stub headers, and passes a PC logic check (`test/host_check.cpp`). **Not built with PlatformIO for ESP32, not flashed, not tested on hardware.**

## What changed in the revision

- Builds as C++11 (button struct has a constructor).
- Software current limiter: each frame's estimated draw is scaled to stay under `LIMIT_MA` (default 1000 mA). It is an estimate (20 mA per colour channel at full, 1 mA idle per pixel), **not a fuse**.
- Layout chosen at build time: default 144 LEDs/m, V5.1 layout (ring 50, hand 23, crystal 11 = 84; the crystal is the end of the hand strip); `-DLAYOUT_60` for 21/10/4; `-DRING_ONLY` for the ring alone.
- Chase is a comet whose speed and tail scale with the pixel count (one ring revolution in 1.4 s).
- Periodic effects no longer drift after hours of run time.
- Pins and limit can be set with build flags; see `platformio.ini`.

## Controls

Button A: short = next effect (breathe → charge → chase → surge → sparks); long = lights on/off; double = two steps.
Button B: short = brightness step (4 levels); double = one-shot flash then resume; long = palette (blue → violet → magenta).

## PC logic check

```
cd electronics/firmware/test
g++ -std=gnu++11 -Wall -Wextra -Istub host_check.cpp -o host_check && ./host_check
```
It simulates button presses and time, checks the effect cycle, flash-and-resume, brightness, palette, on/off, `millis()` rollover, and that no frame's estimated current exceeds the limit. Add `-DLAYOUT_60`, `-DRING_ONLY` or `-DLIMIT_MA=600` to check other builds. It does not test timing on real hardware, the LED driver, or actual current.

## Before trusting it on hardware

Build with PlatformIO, flash, test with 3–5 pixels first, confirm colour order, measure real current against the limiter's estimate, and check button feel with gloves. Reference pins are for an ESP32-WROOM DevKit (16/25/26); a XIAO needs different pins.
