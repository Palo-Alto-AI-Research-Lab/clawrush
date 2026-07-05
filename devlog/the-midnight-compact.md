# devlog: the-midnight-compact (episode 12)

Dry build log for episode 12 of the content factory. Human-readable narrative version: [the longread](../longreads/the-midnight-compact.md).

## Source

- Founder voice memo, 2026-07-05 01:00 (Telegram voice-archive channel, auto-transcribed by bot).
- Topic: recovering a nearly exhausted Claude Code session budget with the /compact command; observed compression and the working rule derived from it.

## The incident (as recorded, de-dramatized)

- Context: long-running Claude Code session, live task in progress, 1 AM local; 2-3% of the subscription token window remaining.
- Action: ran `/compact`, Claude Code's built-in context-compaction command.
- Observed effect (founder's own numbers): session history of roughly 500-900k tokens compacted to about 100k. Decisions, file paths, exact values and agreements survive; conversational bulk is discarded.
- Outcome: several additional hours of productive work on the remaining budget; the task was finished the same night.

## Mechanics (plain summary)

- A long session carries its entire transcript as context; late in a session most of it is low-value conversational history.
- `/compact` asks the model to rewrite the transcript into a dense summary and continues the session on top of the summary instead of the full history.
- Compaction preserves what forward work needs (decisions made, open TODOs, key paths/values) and drops repetition, dead-end debugging and verbose intermediate output.

## Working rules adopted

- Compact proactively on long sessions, before the budget warning - "mid-air refueling before the warning light".
- Keep a per-project compact instruction (what must survive compaction verbatim: decisions, paths, exact values, counters, open issues) so compaction is loss-aware rather than generic.

## Pipeline trace

1. S4 triage: `voice_triage.py append` → post-material record (public, voice, hub:3517).
2. `seed-episode` → episode seed JSON → S5 `episode_adapter.py new --from-seed` → tier drafts.
3. Author-voice tiers written by the top-tier model per the routing rule; deterministic gate `episode_adapter.py check` (teaser 240-370 HARD).
4. Draft-first review; GitHub tier published first (per operator decision 2026-07-05), Telegram tiers scheduled for the next day.

## Notes for reuse

- "Tool-magic" episodes (one command, concrete before/after numbers, a night saved) are cheap to produce and highly relatable; the founder's own numbers (500-900k → ~100k, 2-3% budget left) carry the story without embellishment.
- The human-style guide (no staged scenes, no episode numbering in text, no CTA into non-existent comments, brief co-founder intro) was applied from the first draft this episode - first episode written under the guide rather than edited into it.

---

The full story, in two versions:
📖 For humans, the longread: [../longreads/the-midnight-compact.md](../longreads/the-midnight-compact.md)

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

✔️Invented by Mycroft and Tony,
Palo Alto AI Research Lab.
Proudly made in Silicon Valley 🌉
