# Agent session logs

Create **one uniquely named session file per agent and task**: `YYYY-MM-DD_<agent>_<task>.md`, using `notes/templates/Agent_Session_Template.md`.

**After EVERY action**, successful or failed, record it in that session file and update the shared `HANDOFF.md` before the next action. Include inspections, file reads, commands, code/CAD edits, tests, decisions and tool errors. Tracking-note writes are exempt from recursive logging.

Avoid multiple agents editing the same session file. Rebase/merge before updating shared `HANDOFF.md`; never overwrite another agent's unresolved issues. Commit/push at atomic checkpoints, and disclose UNSYNCED work.
