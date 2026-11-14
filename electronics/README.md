# Vi gauntlet animated lighting — design review package

**PROPOSED, NOT PURCHASED, NOT BENCH-TESTED.** Captures the earlier owner discussion for independent Claude review. V4 received NO-GO; **V5 is the current unprinted draft**. No permanent holes or CAD edits authorized by this package.

- **Two gauntlets, independent**: 1 ESP32-class controller, 2 momentary thumb-reachable buttons and 1 protected 5 V USB power bank **per gauntlet** (totals: 2 boards, 4 buttons, 2 banks).
- **Effects agreed**: idle breathing, charging, energy chase, power surge, flash/special attack, arcane sparks/overload; blue/cyan with violet/magenta accents. See [EFFECTS](EFFECTS.md).
- **Firmware**: WLED + presets/buttons is the **preferred path**. [wled/presets.json](wled/presets.json) is a proposed configuration; [firmware/src/main.cpp](firmware/src/main.cpp) is a **separate, alternative** ESP32 Arduino reference for exact one-shot flash, not a WLED extension. Neither is device-tested.
- **Parts**: [BOM](BOM.md); **wiring**: [WIRING](WIRING.md); **review tasks**: [REVIEW_CHECKLIST](REVIEW_CHECKLIST.md).

**Measured from original CAD by Claude, not physical**: ring trough 27.1 mm radial width × 13.3 mm depth, outer-wall circumference ~351 mm; back-of-hand strip window 13.3 mm wide × 1.56 mm thick × 238 mm long; crystal reference 37 × 10 × 65 mm. The ring wall *may* accommodate bare 8 or 10 mm RGB strip, but cover closure, wire exit and actual printed V5 fit remain untested. Earlier ~2.7 mm narrow accent strip idea is also unverified. **V5 hand/crystal lighting and mounts are not yet restored.** See [Claude audit](../audits/results/ELECTRONICS_FIT.md) and [V5 README](../releases/v5/Vi_Gauntlet_X1C_V5_Draft/README_V5_DRAFT.md).

**Provisional software LED count per arm**: ring 21 + hand 14 + crystal 4 = 39, assuming 60 LED/m ring/hand. Actual strip SKUs, pixel order, protocol, bend direction, electrical draw, connectors and fit must be measured before purchase.

**Strip selection reviewed by Claude, 2026-11-14:** see [LED_STRIP_COMPARISON](LED_STRIP_COMPARISON.md). Recommended: BTF-LIGHTING Ultra-Narrow WS2812B 3535, 144 LEDs/m, 7.2 mm for ring, hand and crystal (50 + 34 + 9 = 93 px per arm). Conditional on the T-1 fit test; hand and crystal need unapproved V5 CAD changes.

**Code, WLED and wiring review (Claude, 2026-11-14, reading only):** [CODE_AND_WLED_REVIEW](CODE_AND_WLED_REVIEW.md).
