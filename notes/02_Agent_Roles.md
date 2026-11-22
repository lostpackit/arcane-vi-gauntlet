---
type: agent-roles
tags: [agents, coordination]
---

# Agent roles and boundaries

| Agent | Intended role | Shared rules |
|---|---|---|
| Claude Code | Independent geometry/slicer/assembly audit and justified CAD corrections | `CLAUDE.md`, `AGENTS.md` |
| ChatGPT | Design iteration, review of findings, engineering documentation | `AGENTS.md` |
| GitHub Copilot | Local scripts, tooling and repository improvements | `.github/copilot-instructions.md` |
| Hermes | Repeatable automation, build tooling and coordination when configured | `HERMES.md` |
| Gemini / others | Additional independent analysis | `GEMINI.md`, `AGENTS.md` |
| Human owner | Physical prints, fit checks, purchase decisions and final sign-off | Release gates |

**Claude conversations by topic (2026-11-22):** Main, Electronics & LEDs, Print queue, Mechanics (optional), Finishing; ownership and starter prompts in [[Conversation_Starters]].

These are suggested roles, not claims that agents are running or connected. Each agent must read [[HANDOFF]] and update it plus its own session note after every action. No agent may unilaterally declare the wearable production-ready without evidence.
