# devlog: the-thirty-dollar-aqueduct (episode 11)

Dry build log for episode 11 of the content factory. Human-readable narrative version: [the longread](../longreads/the-thirty-dollar-aqueduct.md).

## Source

- Founder voice memo, 2026-07-03 21:37 (Telegram voice-archive channel, auto-transcribed by bot).
- Topic: standing up an always-on cloud clone of the whole system (a VPS "anchor node") after a home-hardware failure; closing the "aqueduct" cliffhanger from episodes 9 and 10.

## Incident (episode 4 recap, de-dramatized)

- A GPU upgrade coincided with a motherboard-or-PSU failure on the primary home machine; exact culprit undetermined.
- Impact: the machine hosting the knowledge vault, agents and sync hub went down entirely; recovery relied on spare RAM bought years earlier.
- Root cause framing: single-machine architecture, not the failed part. A ~$100 component had company-wide blast radius.

## Architecture (as built, generalized)

- **Anchor node**: a small always-on VPS (budget hosting tier, ~$30-50/month all-in) that carries a clone of the system: vault, agent runtime, sync endpoint.
- **Mesh VPN**: all machines (home, work, cloud) join one private mesh network; the anchor is reachable regardless of home NAT/ISP state.
- **Continuous file sync**: bidirectional synchronization between all nodes; a file created on any machine propagates to all others within seconds. The cloud copy makes the fleet survive any single home node dying.
- **Witness/heartbeat**: a periodic tick on the anchor observes node liveness; a silent node is flagged as an incident (same "silence is never consent" rule as the agent-consensus layer from episode 10, applied to hardware).
- Design principle: Kalashnikov simplicity - stock VPS, stock sync, small watchdog scripts; every part repairable by a non-technical operator.
- Privacy note: node addresses, hostnames and network identifiers are deliberately omitted from all public tiers.

## Cost

- $30-50/month total for the anchor tier as stated in the source memo; no enterprise services involved.

## Status

- Anchor node live and in daily use; home machines now function as replaceable "taps" rather than the single point of failure.
- Failure drill still informal: the architecture has survived real home-hardware death once (the founding incident), scheduled kill-tests are a candidate next step.

## Pipeline trace

1. S4 triage: `voice_triage.py append` → post-material record (public, voice, hub:3513).
2. `seed-episode` → episode seed JSON → S5 `episode_adapter.py new --from-seed` → tier drafts.
3. Author-voice tiers written by the top-tier model per the routing rule; deterministic gate `episode_adapter.py check` (teaser 240-370 HARD).
4. Draft-first review; publishing only on explicit human approval.

## Notes for reuse

- Payoff episodes work: a cliffhanger promised twice (episodes 9 and 10) and then delivered reads as narrative reliability; the audience sees promises kept.
- Concrete price anchors ($30-50/month vs. a family dinner) make infrastructure stories relatable to non-technical readers.
- Cross-episode rules ("silence is an incident") are becoming the show's recurring vocabulary; reusing them compounds recognition.

---

The full story, in two versions:
📖 For humans, the longread: [../longreads/the-thirty-dollar-aqueduct.md](../longreads/the-thirty-dollar-aqueduct.md)

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

✔️Invented by Mycroft and Tony,
Palo Alto AI Research Lab.
Proudly made in Silicon Valley 🌉
