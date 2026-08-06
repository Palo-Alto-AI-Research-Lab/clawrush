# A Trigger on Volume

Another rule for my agent. [It follows the one about recall.](recall-first-then-hand-me-a-prompt.md)

It needs a trigger on volume. If a task requires genuinely large research, a lot of tokens, long reasoning, heavy computation, it does not carry that itself.

Instead:

It estimates the size of the operation: can it handle this, or is the chunk too big.

If the chunk is too big, it prepares a package for me: the data needed, the context, and a ready-made prompt that I simply paste into another LLM.

Plus an instruction on exactly what to bring back.

I run that in an external deep research and bring the result back to the agent.

What is left is to define what counts as large and in which cases the agent is obliged to delegate. That needs thinking through and writing down as rules.

## The part that decides whether delegation works

Everyone gets the first half right and skips the second. The first half is "hand me a prompt". The second half is the return contract, and without it the whole loop leaks.

**The return instruction is the load-bearing piece.** An external model handed a bare question returns an essay. An essay has to be read by a human, interpreted, and retyped into whatever the agent actually needed, which is exactly the work delegation was supposed to remove. Say what comes back and in what shape: these fields, this format, sources with dates, and the explicit sentence "if you could not verify X, say so rather than filling the gap". Otherwise the package saves ten minutes and costs thirty.

**A package is data plus context plus prompt, in that order.** The external model has none of your history. If the package does not carry the relevant slice of what is already known, the outside answer re-derives things you settled weeks ago and contradicts them with confidence.

**Delegation needs a number, not a feeling.** "This is large" is not a trigger, it is a mood. Something has to be countable: how many sources need reading, how much context the task drags in, how many independent claims need verifying. We have not landed on that number either, and pretending otherwise would be the kind of stale claim that has bitten us before.

**And it needs an end.** A delegated research request that comes back and is never applied is worse than one never sent: it cost money and time and it now sits in a registry looking answered. Every request closes as applied, with what changed, or parked, with why.

The honest state: the packaging half is real and we run it. The trigger half, the automatic decision "this is too big for me", is the open question in the post and it is still open here.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it. Previous rule: [Recall First. Then Hand Me a Prompt.](recall-first-then-hand-me-a-prompt.md)
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
