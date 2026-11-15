---
type: agent-session
agent: Claude (Claude Code, cloud session)
task: Model re-check, digital simulation, V5.2, GitHub issues
date: 2026-11-15
status: complete
tags: [session, v5, simulation, issues, claude]
---

# 2026-11-15 — Claude — V5.2 simulation and issue queue

No printer, no hardware, no Bambu Studio. Everything here is computed.

## Log

1. Pulled `main`; GitHub issues reachable through the REST API (GraphQL is blocked for this session).
2. Assembly simulation, first run: killed by the memory limit (surface-distance query on the full union). Rewrote it to use solid-to-solid minimum-gap queries.
3. Second run exposed three problems in my own models of the hardware, not in the shells: cover assumed 0.3 mm low (measured seat is 0.25 mm), ring strip band centred on the ring's centre of mass instead of the true trough axis (0.3 mm off), and a 34-LED hand strip longer than the 232.5 mm deep channel. Fixed the first two in the simulation; the third is a real correction: **33 LEDs**.
4. Wire-path test: first grid did not cover the hand channel (wrong direction); redone. Result: trough → hand channel passed only a **2.0 mm** sphere in V5.1. Trough → arm cavity 11 mm.
5. V5.2 build: added a 9 mm wire slot (3 mm³ removed, shell 08 only) → 4.0 mm.
6. Gauge magnets: first build cut pockets where the gauge does **not** touch the shell (9 mm air gap). Contact analysis showed only narrow rims. Removed the pockets; rebuilt. Gauge insert unchanged.
7. Finger fit: most reference finger bodies are not valid solids, so the boolean test failed; switched to surface sampling. Cores clear shells 12/13 by 0.8–1.8 mm; slot pieces overlap at most 0.15 mm.
8. Thumb seat: reference thumb base overlaps shells by up to 2.05 mm; printable thumb base is a different revision. Logged on issue #14.
9. Mount concepts built and fit-checked against a handle cylinder and 12 × 12 mm switch bodies.
10. Surrogate slices of shells 08 (V5.2), 10–13, inserts and mounts: all slice; unsupported-branch warnings on 08, 12, 13.
11. Created labels and issues #2–#19; closed #17–#19 with evidence.
12. Updated firmware layout (83), presets, order list, READMEs, audit addendum; PC firmware check PASS.

## Not done

Bambu Studio slicing, any print, any wiring. Supports re-orientation (#15). Seam relocation (#16). Thumb string route (#14).

## Sync

Docs, records, scripts PUSHED. V5.2 CAD (4 files) delivered as `V5_2_changed_files.zip`; upload tracked in issue #2.
