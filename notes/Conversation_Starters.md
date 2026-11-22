---
type: start-here
tags: [agents, coordination, claude-project, start-here]
updated: 2026-11-22
---

# Claude conversations: who owns what, and how to start each one

Owner decision 2026-11-22: work is split into topic conversations inside the Claude Project "Arcane Gauntlets". Each conversation **owns** its files; others read them freely but **ask before editing** (through Erich or a note in `notes/inbox/`). Shared logs ([[03_Decision_Log]], [[04_Test_Log]], [[HANDOFF]] entries) are append-only for everyone. Always fetch/rebase before writing.

| Conversation (chat title) | Owns | Start Here |
|---|---|---|
| **Main** (was "LED review") | `HANDOFF.md` current-state block, [[00_Project_Hub]], `AGENTS.md`, this file, deadline plan, cross-topic questions, "clean up the vault" | [[HANDOFF]] |
| **Electronics & LEDs** | `electronics/` (incl. `concepts/`, WLED, firmware, sled/cover/button pod), [[LED_Wiring_Start_Here]] | [[LED_Wiring_Start_Here]] |
| **Print queue** | [[Print_Queue_Start_Here]], print packs and `PRINT_ORDER`, inventory, slicer settings, print history, LFS upload list | [[Print_Queue_Start_Here]] |
| **Mechanics** (optional; the thumb conversation can become this) | fingers, strings, thumb, handle, dowels, any shell CAD change (owner approval required) | `releases/v5/.../README_V5_DRAFT.md` |
| **Finishing** | [[Finishing_Start_Here]]: glue-up order, adhesives, sanding/priming/painting, masking clear parts, final assembly and wearing checklist | [[Finishing_Start_Here]] |

Cross-topic hand-offs that must not be missed:
- Electronics → Finishing: strip threaded (ring + hand channel) **before** lenses/cover are bonded; sled glued under the ring; wires routed before seams close where they pass a seam.
- Print → everyone: what is actually printed (owner report) goes in [[04_Test_Log]].
- Any new 3MF/STL from Claude is LFS: list it in HANDOFF "Owner upload needed".

## Starter prompts (paste as the first message of a new chat in the Project)

**Main**
> You are the **Main / coordinator** conversation for my Arcane Vi Gauntlet. Sync the repo and read AGENTS.md, HANDOFF.md, notes/00_Project_Hub.md and notes/Conversation_Starters.md; do the vault hygiene check. You own the HANDOFF current state, the Project Hub, AGENTS.md and the deadline plan; other topics belong to their conversations (see Conversation_Starters), so don't edit their files. First: give me a day-by-day plan to 2026-11-28 across printing, electronics, mechanics and finishing, and the open decisions blocking it.

**Print queue**
> You are the **Print queue** conversation for my Arcane Vi Gauntlet. Sync the repo, read AGENTS.md, HANDOFF.md, notes/Conversation_Starters.md and notes/Print_Queue_Start_Here.md; do the vault hygiene check. You own the print queue, print packs, inventory, slicer settings and print history; don't edit other conversations' files. First: list what is printed, what is left for each arm, and the X1C / A1 Mini plate schedule to 2026-11-28.

**Mechanics**
> You are the **Mechanics** conversation for my Arcane Vi Gauntlet (fingers, strings, thumb, handle, dowels, shell geometry). Sync the repo, read AGENTS.md, HANDOFF.md, notes/Conversation_Starters.md and releases/v5/Vi_Gauntlet_X1C_V5_Draft/README_V5_DRAFT.md; do the vault hygiene check. No shell geometry change without my approval. First: status of the thumb joint and the finger string test, and what I need to test physically next.

**Finishing**
> You are the **Finishing** conversation for my Arcane Vi Gauntlet: glue-up, sanding, priming, painting, masking the clear parts, final assembly. Sync the repo, read AGENTS.md, HANDOFF.md, notes/Conversation_Starters.md, notes/Finishing_Start_Here.md and notes/LED_Wiring_Start_Here.md; do the vault hygiene check. Respect the electronics install order (strip and wiring before anything is bonded over them). First: a glue-up and paint plan for both arms working back from 2026-11-28, with dry times and what must be installed before each glue step.

**Electronics & LEDs** (this conversation; for a fresh one later)
> You are the **Electronics & LEDs** conversation for my Arcane Vi Gauntlet. Sync the repo, read AGENTS.md, HANDOFF.md, notes/Conversation_Starters.md and notes/LED_Wiring_Start_Here.md; do the vault hygiene check. You own electronics/ and the LED Start Here note. Continue from the Start Here "Next steps".
