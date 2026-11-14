---
type: agent-session
agent: Claude (Claude Code, cloud session)
task: Ring LED strip comparison before purchase
date: 2026-11-14
status: complete
tags: [session, electronics, leds, claude]
---

# 2026-11-14 — Claude — LED strip comparison

Owner asked for a final comparison of three BTF-LIGHTING WS2812B strips for the V5 ring before ordering. No purchase, no hardware, no CAD change.

## Log (UTC, approximate)

- **22:10** Pulled `main` (`23fc45e`). Read `electronics/` pack (BOM, wiring, effects, WLED presets, standalone firmware, review checklist) and the ChatGPT session note.
- **22:14** Web research on the three strips. Manufacturer page confirms the ultra-narrow variant: 3535, 144 LEDs/m, 7.2 mm, IP30, white PCB, 0.3 W/LED, cut at every LED. It does not state thickness, pitch or bend radius.
- **22:16** Standard WS2812B product page could not be fetched (blocked by the session's URL allowlist). Used the BTF collection page, the BTF listings on Amazon.de and buyer reports instead. The 144/m 5050 strip is listed as 10 mm but buyers measure about 12 mm or more.
- **22:20** Re-measured the V5 ring: cover seat at h ≈ 9.5 (0.3 mm lower than the original part), floor −3.50, so about 13.0 mm usable wall height; outer wall r 55.9, inner 28.8. Computed LED counts, joint gaps and local bend radii for each option.
- **22:30** Wrote `electronics/LED_STRIP_COMPARISON.md`; appended review sections to BOM, WIRING, EFFECTS, WLED README, electronics README, audit electronics-fit report; added `electronics/wled/presets_144.json` (segment bounds remapped only; original untouched).
- **22:35** Updated handoff, test log, action log; committed and pushed.

## Result

Recommend the 7.2 mm 3535 144 LEDs/m strip for ring, hand and crystal (50 + 34 + 9 = 93 px per arm), WLED limit 1000 mA to start. Conditional on T-1 with a real sample. Hand and crystal need V5 CAD changes that are not approved.

## Not done

Did not verify an Amazon.de listing for the ultra-narrow strip. Did not compile `main.cpp`, load presets on a device, or complete the other items on `electronics/REVIEW_CHECKLIST.md` (board choice, button pod, voltage-drop calculation, mounts).

## Sync

PUSHED with the commit that adds this file.
