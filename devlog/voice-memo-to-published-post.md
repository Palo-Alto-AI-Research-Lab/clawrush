# devlog: voice-memo → published-post pipeline, run 2026-07-05

Dry log of one full pipeline run. Human narrative: see longread-en.md (same directory).

## Input
- Source: 2 voice memos dictated on a smartwatch while swimming, 2026-07-05 ~14:00 Lisbon.
- Capture requirement (house rule): recording device always on the operator; 30-second capture beats "remember later" (measured loss otherwise: ~100% of night thoughts).

## Pipeline stages
1. STT: Whisper transcription. Policy: transcription of the founder's voice always runs on the best available model; no cost-downgrades on this stage (codified rule, treated as a carve-out from normal cost optimization).
2. Summary/normalization: n8n workflow "Personal Audio Summary" (premium LLM tier, same carve-out).
3. Delivery: transcript + summary land in the hub Claude Code session as a task ("write a post on this, weave in our house rules").
4. Authoring: author-voice model tier (Opus-class or above; author voice is never written by a mid-tier model, codified rule). Draft saved to the content-factory drafts folder before anything goes out.
5. Approval gate: final text shown to the founder; explicit "+" required (Tier-2 outbound gate). Nothing auto-publishes.
6. Publish: Claude-in-Chrome MCP drives the founder's own logged-in browser tab. Rate guard (fb_guard.py) checked before (0/8) and recorded after (1/8; hard cap 8 posts/day).
7. Footer: posted as the FIRST COMMENT (body kept link-free): follow link + Calendly + WhatsApp + lab signature. Single source of truth for footer blocks: _STYLE-footer.md.
8. Seed reaction: first like set by the agent (first like is the hardest).
9. Fan-out: episode_adapter.py scaffolds an 8-file bundle (teaser RU/EN, medium, longread RU/EN, Habr, VC.ru, this devlog); each file is a native rewrite per platform, no copy-paste.

## Failure notes (this run)
- First click on the FB composer landed on Stories: the feed shifted during lazy-load. Fix: re-navigate, wait, re-click. No FB warnings triggered.
- FB post dialog is a 2-step flow (compose → post settings); the Post button lives on step 2.
- Multi-line comments: Enter submits; use Shift+Enter for line breaks.

## Core thesis (from the memos, compressed)
A voice memo is not noise; it is an intention. An intention is approximately a well-formed question. Execution cost is collapsing (AI decomposes and implements), so the scarce asset is the intention itself. Therefore: capture 100% of thoughts, transcribe at max quality, process every memo as an intention, decompose, implement.

## Cross-links
- Human longread (EN, canonical): longread-en.md
- Human longread (RU): longread-ru.md
- Published FB post (RU): https://www.facebook.com/AntonyDzi/posts/pfbid02ny4uuwQTeCMhyB7gDLTPec7QzNKcHavjbtgCFjgffsK7p1j8h6QLL5x2Vvkxn5nZl

---
The full story, human version: longread-en.md.
Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct: WhatsApp +1 341 222 9178.
P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.
Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
