# Agent Interface, Not User Interface

I will continue my thought about how I see the near future. There used to be a User Interface, and now every company will build an Agent Interface.

Look at how it went:
- before, a person went and bought at the pizzeria themselves;
- then the user's agent went and tried to buy something on the pizzeria's website, but clicking through the site in Chrome was very hard for it;
- and now the user's agent interacts with the pizzeria's agent.

So if before we had User Interface and User Experience, now we get Agent Interface and Agent Experience.

And agents really can talk to each other in their own format: over MCP, over A2A, or something else.

That is why I want this topic researched deeply. What popular cases already exist where one company's agent talks to another company's agent?

## What actually changes when the user is a program

The interesting part is not the protocol. It is which properties of a good interface survive the switch and which invert.

**Affordances disappear, so semantics have to be explicit.** A human looking at a button labelled "Order" infers a great deal from context: the price above it, the address in the corner, the fact that a second click would charge twice. An agent infers none of that. Everything a screen communicated implicitly has to become an explicit field: units, currency, timezone, whether this call is idempotent, what happens on retry.

**A dry run stops being a nicety and becomes a core verb.** Humans preview by looking. An agent cannot look. If your interface has no way to say "tell me what this would do without doing it", every integration test happens in production, and the first bug order is a real pizza at a real address.

**Errors are read by a machine, so they have to be actionable, not polite.** "Something went wrong, please try again later" is a dead end for an agent: it cannot tell a transient failure from a permanent one, so it either retries forever or gives up on something that would have worked in ten seconds. Machine-readable class, whether retry is meaningful, and after how long.

**Rate limits and quotas become a safety layer, not a pricing one.** One buggy loop on the other side turns into thousands of calls in minutes. That is now their bug and your incident.

**And someone still has to be accountable for the irreversible step.** Two agents can negotiate an order beautifully and both be wrong about the address. Somewhere in the chain a human has to own the moment money moves or a message goes out under someone's name, or the whole thing is an automated way to make confident mistakes at scale.

On the question at the end, the honest answer: we do not have a verified list of company-agent-to-company-agent cases in production, and we are not going to invent one. MCP and A2A exist as protocols, which is not the same as a market of live integrations. That is a real research question, and the useful version of it is narrower: find cases where a transaction with money or a commitment completed between two organisations' agents without a human in the middle, and check what they did about the five points above.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it. Related: [Letting Someone Else's Agent Into Your Database](letting-someone-elses-agent-in.md).
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/agent-interface-not-user-interface.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
