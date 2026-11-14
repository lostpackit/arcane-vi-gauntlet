# Agent synchronization protocol (Obsidian + GitHub)

This is a mandatory extension of `AGENTS.md`. The repository root is the Obsidian vault; **`HANDOFF.md` is the single shared handoff**, and dated `notes/sessions/` files are detailed per-agent records. GitHub `main` is the common remote.

## 1. Start every agent session
1. Check `git status`, `git branch --show-current`, `git fetch origin`.
2. If clean, `git pull --rebase origin main`; if not, protect local edits and reconcile without overwriting.
3. Read `AGENTS.md`, `HANDOFF.md`, `notes/00_Project_Hub.md`, `docs/PROJECT_BRIEF.md`, `docs/RELEASE_GATES.md`, and recent session notes.
4. Open a unique session log at `notes/sessions/YYYY-MM-DD_<agent>_<task>.md` from `notes/templates/Agent_Session_Template.md`. Use UTC times where possible.
5. Check the actual Git LFS assets; docs referencing paths do not prove files exist.

## 2. AFTER EVERY ACTION — required
For **each action**, including a file read/inspection, edit, test, command, tool operation, decision, failure, or attempted remote write:
- Add a dated, factual entry to your own session note: action, observed result, evidence, files, next step.
- Update `HANDOFF.md` with the same **latest state**, the next action and blockers; keep previous unresolved findings.
- Update relevant engineering note, decision log, test log and/or acceptance gate if the action affects them.
- Save these notes **before the next project action**. Writing these tracking notes is exempt from triggering another recursive log entry.
- At each completed atomic work unit, **commit and push**; verify the remote commit. Do not mark `PUSHED` until confirmed.
- If a tool cannot write, provide the proposed exact changes and say **UNSYNCED**; if offline, retain local notes and sync when able.

This is an instruction to agents, **not** a background daemon or a guarantee that every third-party assistant obeys it. A failed or absent push means the other agents will not see the update.

## 3. Prevent concurrent edits from clobbering each other
- Prefer a task branch for CAD changes; do not push unfinished CAD onto `main`.
- Use a unique per-agent session filename to avoid log conflicts.
- Before updating the shared `HANDOFF.md`, fetch/rebase newest changes and merge all other agents' unresolved issues.
- Never force-push `main` or overwrite another agent's evidence.
- On a handoff merge conflict, preserve both agents' actions, add a conflict-resolution note, and do not declare synced until pushed.
- One shared `HANDOFF.md` summarizes the latest state; detailed history lives in per-agent session notes and Git commits.
- Do not store secrets, personal data, tokens or private credentials in Obsidian notes.

## 4. Handoff entry format
```markdown
### YYYY-MM-DDTHH:MM:SSZ — <agent>
- Action:
- Result: PASS / FAIL / UNKNOWN / BLOCKED (with facts)
- Files changed:
- Evidence (file, command output, commit, issue):
- New risks / decisions:
- Next action:
- Sync: LOCAL / PUSHED <sha> / UNSYNCED <reason>
```

## 5. Release status is evidence-based
A PASS must reference a reproducible test, measurement, slicer output or physical fit. A closed STL mesh alone does not clear a release gate. For V4, the authoritative status remains **NOT APPROVED** until the checks in `docs/RELEASE_GATES.md` pass.

## 6. When the user is uploading CAD
The user may be working in a cloned repo while documentation commits land. Before their asset push:
```powershell
git status
git pull --rebase origin main
git lfs ls-files
git push origin main
```
If the worktree is dirty or commits conflict, do not force the push. Commit/stash local work carefully and reconcile first. Existing user files must never be discarded.
