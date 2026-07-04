# devlog: from-chat-to-workflow (episode 8)

Dry build log for episode 8 of the content factory. Human-readable narrative version: [the longread](../longreads/from-chat-to-workflow.md).

## Source

- Founder voice memo, 2026-06-28 (Telegram voice-archive channel, auto-transcribed by bot).
- Topic: a plain-words taxonomy of the six agent primitives and their relative token cost.

## The taxonomy (as recorded, de-dramatized)

1. **Chat**: single request/response, no persistence, cheapest.
2. **Skill**: a repeated request externalized into an instruction file (skill.md), loaded on trigger. Heuristic: the third repetition of the same ask is the signal to extract a skill.
3. **Goal**: a loop of act → verify → retry until goal == completed; the operator supplies the outcome, not the steps.
4. **Subagent**: child agents with separate context windows, orchestrated by the main agent; used for parallel research digs with a merge step.
5. **Team**: agents communicate peer-to-peer (negotiate, split work). Materially higher token cost: inter-agent chatter is billed like any other tokens. Production instance: cross-machine consensus between the project's computers.
6. **Workflow**: inversion of control; deterministic code orchestrates many agents (fan-out, collect, verify, repeat). Repeatable and auditable; effectively a program whose functions are agents.

## Cost gradient and the selection rule

- Token cost rises monotonically down the list; so does autonomy.
- Selection rule adopted: use the lowest primitive that solves the task ("don't haul bread in a semi-truck"). Email → chat; recurring routine → skill; wide research → subagents; project-wide audit → workflow.
- Failure mode observed in the wild: teams-of-agents applied to single-step tasks, burning tokens for no quality gain.

## Production notes (this factory)

- Skills run the content pipeline itself (episode scaffolding, length gates).
- Subagents: parallel research with independent context windows, merged by the orchestrator.
- Team: machine-to-machine consensus bus between the project's computers (see the earlier courier episode and its devlog).
- Workflow: deterministic scripts orchestrate multi-agent checks; the LLM is only called where judgment is needed. Rule of thumb reused from an earlier episode: recurring service tasks should not call the LLM at all.

## Notes for reuse

- The six-primitive ladder doubles as a cost-control checklist: before spawning agents, name the step you're on and the step the task needs.
- Educational-episode pattern: taxonomy posts inherit a poll-style audience question (which step are you on) across all tiers.

---

The full story, in two versions:
📖 For humans, the longread: [../longreads/from-chat-to-workflow.md](../longreads/from-chat-to-workflow.md)
🤖 For machines: this devlog is written for you. Hand this repo to your coding agent (Claude Code, Codex, Cursor); the pipeline scripts named above are real.

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
