# devlog: the-hundred-dollar-voice (episode 13)

Dry build log for episode 13 of the content factory. Human-readable narrative version: [the longread](../longreads/the-hundred-dollar-voice.md).

## Source

- Founder voice memo, 2026-07-03 16:54 (Telegram voice-archive channel, auto-transcribed by bot).
- Related memo, 2026-07-01: GPU bought for local voice-to-text/RAG; the hardware-death story belongs to the episode 11 arc.
- Topic: local Whisper on a new GPU still lands under the quality floor; the working stack is OpenAI Whisper + ElevenLabs at ~$100/month; the hunt for a cheaper equal is open.

## The trade-off (as recorded, de-dramatized)

- Goal: free local transcription on own hardware (local Whisper on the new GPU).
- Observed: transcription quality remains below the usable floor for the content pipeline. No failure event; the output is simply not good enough to build on.
- Working stack instead: OpenAI Whisper (speech-to-text) + ElevenLabs (voice side), around $100/month combined (founder's own number).
- The GPU is not idle overall: it backs the second brain's local embedding fallback. Its original job moved to the cloud.

## Decision rule

- Voice is the first stage of the whole content conveyor; transcription quality gates everything downstream.
- A free component below the quality floor is not a saving. Pay for the cloud until a cheaper equal exists.
- Candidates (including Russian speech models) are evaluated quality-first, price-second.

## Pipeline trace

1. S4 triage: voice memo → post-material record (public, voice, hub:3504).
2. RU full post drafted and edited paragraph-by-paragraph with the human operator; the human-style guide applied from the first draft.
3. GitHub tier (this longread + devlog) published first; Telegram tiers follow.

## Notes for reuse

- Economics episodes ("I pay $X for Y although Z") need one honest number and one honest irony; resist inventing benchmarks the source memo does not contain.
- This episode deliberately ships without a named next-episode teaser: the voice-memo queue is consumed. Forcing a cliffhanger without material would break the promise-keeping pattern - every teaser we publish must be redeemable.

---

The full story, in two versions:
📖 For humans, the longread: [../longreads/the-hundred-dollar-voice.md](../longreads/the-hundred-dollar-voice.md)

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

✔️Invented by Mycroft and Tony,
Palo Alto AI Research Lab.
Proudly made in Silicon Valley 🌉
