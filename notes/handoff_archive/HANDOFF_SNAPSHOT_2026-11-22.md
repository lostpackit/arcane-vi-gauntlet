---
type: handoff-archive
period: 2026-11-18 to 2026-11-22 09:20
---

# Handoff entries archived 2026-11-22 21:35 (verbatim)

Moved out of `HANDOFF.md` by the vault hygiene check (file was 128 lines). Nothing edited. [Current handoff](../../HANDOFF.md).

### 2026-11-22 09:20, Claude
- Owner decision: continuous strip ring→hand; near end keeps factory connector to ESP32 pigtail (owner soldered pigtail to board). Far end cut before threading. Recorded in Decision Log + LED_Wiring_Start_Here. Next: bench test, then physical turn check. Sync: PUSHED.

### 2026-11-22 09:10, Claude
- Owner photo: strip test-placed in R_08 ring trough; JST connector lies in the trough. Confirmed plan: no connectors in the ring; solder wires at strip ends, exit via hole, connector in cavity. Added to LED_Wiring_Start_Here. Sync: PUSHED.

### 2026-11-21 23:35, Claude
- Bug: all Claude 3MFs show as "geometry_0" in Bambu. Fixed object names (= file name) in a new `Vi_Gauntlet_V5_Print_Pack_named.zip` (geometry unchanged). Repo copies need replacing (issue #21). Owner confirmed X1C plates ("Vi Gauntlet right 3mf_reaggranged") are his project built from Claude's files; plates 21/27 shells still unidentified. Sync: PUSHED.

### 2026-11-21 22:36 CET, Claude
- Claude Project "Arcane Gauntlets": added start-here pointer doc; V4 verdict doc marked historical. Project instructions were empty then; owner has since set them (checked 2026-11-21 22:40). Sync: PUSHED b67fae9.

### 2026-11-21 22:32 CET, Claude
- Added vault hygiene check at every session start (AGENTS.md rule 5a); owner trigger: "clean up the vault". Sync: PUSHED.

### 2026-11-21 22:29 CET, Claude
- Action: Compacted this handoff (was 296 lines). Full previous text archived verbatim at [HANDOFF_SNAPSHOT_2026-11-21](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-21.md). Added "Context continuity" rules to AGENTS.md and the sync protocol, inbox capture for chat-only AIs (`notes/inbox/`), and a paste-in instruction for other AI tools (`docs/AI_CONTEXT_INSTRUCTIONS.md`).
- Next: owner uploads #2/#20; LED bench test in a new conversation starting from LED_Wiring_Start_Here.
- Sync: PUSHED (see git log).

### 2026-11-21 22:26 CET, Claude
- Vault brought current: Project Hub, Decision Log (owner decisions since V5), Test Log, Risks; new `notes/LED_Wiring_Start_Here.md`.

### 2026-11-21 22:17, Claude
- Parts inventory with renders pushed (`Inventory/V5_Parts_Inventory.md`). Retried LFS push of 9 3MFs: still blocked by session network policy. Nothing half-pushed; zip + steps delivered; commented on #2 and #20.

### 2026-11-20, Claude
- Found inverted normals in all five left inserts; fixed copies delivered (hashes in `L_INSERTS_NORMALS_FIX_SHA256.txt`). Session note: `notes/sessions/2026-11-20_claude_a1-mini-translucent-parts.md`.

### 2026-11-19, Claude
- Hardware received and recorded (`electronics/HARDWARE_AS_BOUGHT.md`); firmware/presets set to 91 LEDs, pins 32/14/27.

### 2026-11-18, Copilot SDK
- Backed up local print-pack/source folders to the repo and verified LFS readback of the new objects. Detail in the archive snapshot and `notes/sessions/2026-11-18_copilot-sdk_*`.

