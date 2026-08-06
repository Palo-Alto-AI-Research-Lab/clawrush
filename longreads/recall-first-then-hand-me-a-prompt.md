# Recall First. Then Hand Me a Prompt.

Every time I give Claude Code a task, it must first do this:

1. Search its own memory and history: does it already have something on this topic. If it found something, give it both to me and to itself, so it answers the request better.
2. If nothing was found, or what exists is stale, there needs to be a trigger that recognises exactly that: this content is no longer fresh.

And in that case Claude Code should hand me a block prompt. So that I go to some other LLM myself and run a deep research.

The idea is this. Suppose I want to dig into something seriously. Claude Code searches history and its own memory. Fresh data exists, great, it uses it. Fresh data is thin, or it understands the data is stale, then it always offers: here is a prompt for you, hand it to an LLM and make me a deep research artifact so I can execute your task better.

And this needs to be mandatory for all tasks.

## What this looks like once it is built

Three parts, and the order matters more than any of them individually.

**Recall is a gate, not a courtesy.** It runs before the work starts, not after the agent has already produced an answer worth defending. An agent that answers first and checks its notes afterwards will rationalise, because by then it has a position. Cheapest tools first: a database query and a grep cost nothing, retrieval over a curated vault costs little, sending the whole corpus to a model costs the most and goes last.

**The research request is an artifact, not a chat message.** A deep research ask gets a number before the prompt is handed over, lands in a registry, and names its consumer at birth: who is waiting for this answer and what decision it unblocks. Research with no named consumer is a hobby.

**Fanned out, not bought per unit.** The same question goes to several paid subscriptions at once, and the threshold for done counts rails rather than naming vendors. Where they agree, no manual re-check. Where they diverge, that divergence is the work list.

And one part that is easy to skip and expensive to skip: **research has an end**. Synthesised is not finished. Every request closes either as applied, with a note on what changed because of it, or as parked, with a note on why it was dropped. Otherwise the registry fills with knowledge nobody used, which is indistinguishable from knowledge nobody has.

## The honest gap

The hard part in the post is point two: the trigger that recognises staleness on its own. Deciding "what I have is out of date" automatically is not solved here. What works today is narrower: a verdict expires if it carries no date and no stated way to re-check it, and a cause stated without evidence is labelled a hypothesis rather than a fact. That is a rule, applied by whoever is reading, not a detector that fires on its own.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
