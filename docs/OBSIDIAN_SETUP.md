# Open the GitHub repository as an Obsidian vault

The **Git repository root** is the Obsidian vault; there is no separate database and no copy of project notes elsewhere. Obsidian uses local Markdown, which GitHub and other agents can read.

## Setup
1. Clone `https://github.com/lostpackit/arcane-vi-gauntlet.git` on your computer.
2. Install/open Obsidian. Choose **Open folder as vault** and select the **`arcane-vi-gauntlet` repository folder itself**, not just `notes/`.
3. Start at `notes/00_Project_Hub.md`; pin `HANDOFF.md` for quick access.
4. Core Templates may be enabled in Obsidian Settings; template folder is `notes/templates`. No third-party plugin is required.
5. Before working in Obsidian, pull the latest Git changes; after editing, commit and push. Obsidian edits are **not** automatically shared until Git synchronizes.

## Structure
```text
arcane-vi-gauntlet/
  AGENTS.md                <- universal agent instructions
  CLAUDE.md                <- Claude entry point
  HANDOFF.md               <- canonical live cross-agent handoff
  .obsidian/               <- shareable Obsidian vault settings only
  notes/
    00_Project_Hub.md      <- vault dashboard and links
    01_Engineering_Map.md
    02_Agent_Roles.md
    03_Decision_Log.md
    04_Test_Log.md
    05_Risks_and_Blockers.md
    Action_Log.md          <- milestone index
    sessions/              <- one append-only file per agent/task
    templates/             <- reusable note templates
    assets/                <- optional screenshots and diagrams
  docs/                    <- canonical engineering requirements and release gates
  audits/                  <- independent audit prompts and results
  originals/               <- immutable CAD source assets (Git LFS)
  releases/                <- versioned derived CAD (Git LFS)
```

## Vault conventions
- Markdown with optional YAML frontmatter and Obsidian `[[wikilinks]]`.
- Prefer links to canonical engineering docs instead of duplicating test status in multiple places.
- Name dated session notes `YYYY-MM-DD_<agent>_<task>.md`; use UTC timestamps.
- Keep evidence paths and Git commit references; distinguish verified facts from assumptions.
- Do not commit machine-specific `.obsidian/workspace*.json`, plugin caches or secrets.
- The handoff and agent logs must be updated **after every action** as specified in `AGENTS.md`.
