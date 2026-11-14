# Standalone Arduino firmware — alternative to WLED

**Reference only, not compiled, flashed, or hardware tested.** WLED is preferred; this separate PlatformIO sketch demonstrates the precise effect/button behavior and momentary flash. ESP32-WROOM-32 DevKit, GPIO16 LED data through 5 V level shifter, GPIO25/26 momentary switches to GND. 39 provisional GRB WS2812-compatible RGB pixels: ring 21, hand 14, crystal 4. No Wi-Fi sync.

Button A short cycles breathe/charge/chase/surge/spark; long toggles power. Button B short steps brightness; double triggers a **350 ms one-shot flash and resumes prior effect**; long rotates blue/violet/magenta palette. Non-blocking loop; conservative 128/255 max brightness is **not a hard current limiter**. Compile with PlatformIO and bench test 3–5 pixels first. Claude must review rollover, button timing, animation correctness, board pin and supply safety. Do not flash this over WLED unless intentionally switching firmware.
