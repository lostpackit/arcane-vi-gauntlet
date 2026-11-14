# Six animated effects and two-button operation

| Preset | Name | Ring | Hand strip | Crystal |
|---|---|---|---|---|
| 1 | **Idle breathing** | Soft slow blue/cyan breathing | Dim synchronized glow | Brighter pulse |
| 2 | **Charging** | Progressive circular fill | Fill toward knuckles | Peaks at charge |
| 3 | **Energy chase** | Fast rotating highlight with trail | Traveling highlight | Pulse |
| 4 | **Power surge** | Bright blue burst/decay | Surging wave | Bright peak |
| 5 | **Flash / special attack** | Brief white-blue strobe | Synchronized | Synchronized |
| 6 | **Arcane sparks / overload** | Irregular violet-blue-pink sparkles | Random flicker | Intermittent pulse |

**Per arm**: Button A short = next mode 1–6; A long = lights on/off. Button B short = brightness step; B double = flash; B long = violet/magenta color/palette. Two independent arms; WLED Wi-Fi sync optional, not required. Buttons must work offline and be reachable by thumb while holding the original string-actuated finger handle.

**Important difference**: WLED sample preset 5 is a **sustained strobe** until another preset is chosen; it does not automatically resume. The **alternative standalone firmware** makes the flash a ~350 ms one-shot and returns to the prior mode. Claude should validate a WLED playlist/usermod or recommend which approach is appropriate.

Prototype indexes: ring [0,21), hand [21,35), crystal [35,39), subject to real LED count and wiring. Never assume that V5 already has working hand/crystal light channels. Check visual diffusion, color order, current, heat, safe power-up, button bounce and accidental triggering.

**Claude review note, 2026-11-14:** with the recommended 144 LEDs/m strip the indexes become ring [0,50), hand [50,84), crystal [84,93). See [LED_STRIP_COMPARISON](LED_STRIP_COMPARISON.md) and `wled/presets_144.json`.
