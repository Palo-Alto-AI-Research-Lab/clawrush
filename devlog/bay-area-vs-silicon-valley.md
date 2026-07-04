# devlog: bay-area-vs-silicon-valley (episode 6)

Dry build log for episode 6 of the content factory. Human-readable narrative version: [the longread](../longreads/bay-area-vs-silicon-valley.md).

## Source

- Founder voice memo, 2026-07-03 ~01:00 (Telegram voice-archive channel, auto-transcribed by bot).
- Topic: naming/positioning decision for the footer system of the content pipeline.

## Pipeline trace (voice → published drafts)

1. S4 triage: `voice_triage.py append --bucket post` → post-material record in `posts.jsonl` (visibility=public, source_kind=voice).
2. S4 → S5 handoff: `voice_triage.py seed-episode --slug bay-area-vs-silicon-valley` → episode seed JSON.
3. S5 scaffold: `episode_adapter.py new` → 6 tier drafts (teaser ru/en, medium fb, longread ru/en, devlog) with the tier contract baked into placeholders (lengths, cross-links, canonical, CTA).
4. Writing pass: authorial tiers written by the top-tier model per the model-routing rule (author voice = top-tier model only; grunt tiers = cheaper models).
5. Deterministic gate: `episode_adapter.py check` → hard length gate for teasers (240–370 chars), CTA presence, empty-draft detection. This episode: FAIL=0, WARN=0 on first pass.
6. Review: draft-first. Nothing is published without an explicit human "publish".

## The footer system shipped this episode

- Single source of truth: one style file, `_STYLE-footer.md`. Blocks A–E (two-version story ladder / follow links / talk-to-cofounders / hire-us / signature), RU + EN.
- Tier matrix: teaser = 1 link only; medium = A+B+C+E; longread = A+B+C+D+E; dev-log = A+C+D+E. On Facebook the entire footer moves to the first comment (a link in the body kills reach).
- A live-link registry gates the follow block: only links marked live may enter a published footer. Dormant accounts (an unwarmed Reddit account, X handles without API creds) stay out until ready.
- Signature fixed as: "Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley."

## Naming decision (the actual content of the voice memo)

- Observation: inside the SF peninsula everyone says "Bay Area"; "Silicon Valley" is essentially never used by locals. Outside, the recognition ratio flips: "Silicon Valley" is globally understood, "Bay Area" lands with ~5–10% of a general audience.
- This makes the word pair a reliable insider detector (a shibboleth).
- Decision: the public tagline uses "Silicon Valley", i.e. the audience-facing term, deliberately failing the insider test. Rationale: outbound copy must use the audience's vocabulary; in-group vocabulary is reserved for internal docs.
- Generalized rule adopted for all outbound copy: the audience chooses the words, not the author. Landing pages and posts use search-language, not team-language.

## Notes for reuse

- The shibboleth heuristic is a cheap audience-detection tool: listen to which term an inbound lead uses and you learn where they stand relative to your scene.
- Footer blocks live in one file; editing the file edits every future post. No per-post footer drift.

---

The full story, in two versions:
📖 For humans, the longread: [../longreads/bay-area-vs-silicon-valley.md](../longreads/bay-area-vs-silicon-valley.md)
🤖 For machines: this devlog is written for you. Hand this repo to your coding agent (Claude Code, Codex, Cursor); the pipeline scripts named above are real.

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
