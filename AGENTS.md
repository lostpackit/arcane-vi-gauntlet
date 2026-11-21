# Mandatory agent operating instructions — Arcane Vi Gauntlet

These instructions apply to **every AI agent** working in this repository: Claude, Codex, GitHub Copilot, Hermes, Gemini, ChatGPT, and any successor. If your agent environment has its own instruction file, that file must defer to this one.

## Shared state: Obsidian + GitHub
- The **repository root is an Obsidian vault**. Open the cloned repo as a vault. Notes are under `notes/`; the live cross-agent handoff is **`HANDOFF.md` at the repository root**.
- GitHub `main` is the shared remote source of truth, not an agent's chat history or private notes.
- Read `HANDOFF.md`, `notes/00_Project_Hub.md`, `docs/PROJECT_BRIEF.md`, `docs/RELEASE_GATES.md`, and `docs/AGENT_SYNC_PROTOCOL.md` **before doing project work**. Read `docs/ASSET_MAP.md` before claiming any CAD asset exists.
- Before editing: check `git status` and `git fetch origin`. If the worktree is clean, `git pull --rebase origin main`. If dirty, preserve local changes and coordinate; never discard another agent's work.

## Required after-action synchronization — do not skip
**After EVERY project action, successful or failed**, including inspections, file edits, geometry checks, slicer tests, decisions, tool executions, or GitHub operations:
1. Record what was attempted and the actual outcome in your own dated `notes/sessions/YYYY-MM-DD_<agent>_<task>.md`. Include evidence paths, changed files, tests and failures; use UTC timestamps when available.
2. Update the single shared **`HANDOFF.md`** with the latest verified state, last action, next concrete step, blockers, and owner. Never delete another agent's unresolved findings.
3. If the action changes a decision, test result, or release status, update the corresponding Obsidian note and `docs/RELEASE_GATES.md` as appropriate.
4. Save the updates **before the next engineering action**. Documentation writes themselves are exempt from recursive logging.
5. Commit and push at each completed atomic work unit and before ending or handing off. If offline or push fails, mark **UNSYNCED** in the handoff/session log and tell the user; local notes are not cross-agent synchronization until pushed.

For read-only remote agents that cannot edit files, provide the exact proposed handoff/log patch and explicitly state that the repository was **not** updated. Do not claim a successful sync without verifying the remote commit.

## Context continuity: no AI conversation may lose project knowledge
Conversations end, get summarised, or move between tools (Claude, ChatGPT, Copilot, Gemini, Hermes, phone apps). **The vault is the memory, not the chat.**
1. **Start of every conversation:** read `HANDOFF.md`, `notes/00_Project_Hub.md`, and the topic's *Start Here* note (e.g. `notes/LED_Wiring_Start_Here.md`). Process anything in `notes/inbox/` (merge it into the right notes, then delete the inbox file in the same commit). Do not re-ask the owner for facts already recorded.
2. **During the conversation:** every owner decision goes into `notes/03_Decision_Log.md` and every physical result (print, fit, bench test, purchase received) into `notes/04_Test_Log.md` or `electronics/HARDWARE_AS_BOUGHT.md` **in the same session**, not "later".
3. **Before the conversation ends, or when the owner says "update the vault":** update `HANDOFF.md` (current state + one short entry), the topic Start Here note, and your session note; commit and push.
4. **AIs that cannot write to the repo** (chat-only ChatGPT, Claude.ai without the repo, mobile): at the end of the conversation, output a ready-to-save Markdown note using `notes/templates/Inbox_Note_Template.md` for `notes/inbox/YYYY-MM-DD_<ai>_<topic>.md`, and tell the owner the repo was **not** updated. The next repo-capable agent merges it.
5. **Keep the entry points short:** `HANDOFF.md` under about 120 lines; Start Here notes about one page. When `HANDOFF.md` grows past that, move older entries **verbatim** to `notes/handoff_archive/` (never delete them) and leave a link.
5a. **Hygiene check at the start of every session (before other work):** if `HANDOFF.md` is over ~120 lines, a Start Here note is over about one page, `notes/inbox/` has files, or the HANDOFF "Current state" no longer matches reality, fix that first (archive verbatim, condense, merge inbox, correct the state) and log it. The owner can also ask for this any time with **"clean up the vault"**.
6. **One topic, one Start Here note.** When a new workstream starts (e.g. assembly, painting), create `notes/<Topic>_Start_Here.md` and link it from the Project Hub and the HANDOFF topic table.
7. Never record something as done, measured or bought unless it actually happened; never describe a web page or listing that was not actually opened.

## Concurrent agent safety
- Prefer distinct work branches for CAD modifications and separate dated session logs per agent.
- Before editing the shared handoff, fetch/rebase the newest remote version; preserve all other agents' changes and blockers.
- Never force-push `main`; never silently overwrite a handoff, validation report, or another agent's edits. Resolve conflicts by merging both sets of findings.
- Link important changes to commits/issues/PRs. Update the handoff after merges.
- Never edit `originals/` in place. Use versioned releases/branches for derived CAD. Large STL/3MF/ZIP files require Git LFS.
- Do not commit secrets, access tokens, personal credentials, or unlicensed redistribution.

## Engineering truth standard
- V4 is **a digital candidate, not print-approved**.
- A watertight STL or nominal bed fit is not equivalent to a real X1C sliced, assembled, safe wearable gauntlet.
- Keep original manually string-actuated fingers compatible; motorized knuckles deferred.
- Animated addressable LEDs, buttons, ESP32-class controller and battery are goals; no LED strip width or hardware fit has been physically verified.
- Record PASS/FAIL/UNKNOWN/BLOCKED with evidence, not guesses. Never mark a gate PASS based on another agent's unverified summary.
- Ask the user before irreversible fabrication, purchasing, publishing third-party models, or deleting history.

## Handoff minimum fields
Update `HANDOFF.md` after each action: timestamp, agent, action, observed result, modified files, verification/evidence, open blockers, next action, and sync state. Keep the file short enough to read at session start; put full detail in your own session note.

**On exit:** ensure the handoff is current, your session note is saved, relevant notes/gates are updated, and remote push has been verified or the failure is disclosed.
