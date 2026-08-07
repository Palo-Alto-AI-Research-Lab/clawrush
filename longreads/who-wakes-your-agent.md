# Who Wakes Your Agent?

I think I need to redeploy Invoiceman on the desktop, so that my desktop is all in one place for it.

Claude Code cannot launch itself. It is not an alarm clock, it is an executor: until someone outside says "time", it sleeps.

And that someone is what I want to assemble on my own desktop, in one place.

What has to sit there:
- the vault with all my knowledge, everything I know at all, lying right next to it;
- RAG, that is search over that knowledge, so the agent does not rummage blindly but pulls the needed piece straight away;
- execution, the part that actually does the work with its hands.

And on top, a scheduler that works cron-style: by schedule or by event, it pulls Claude Code and says "this happened, start".

It sounds a bit boring, but this is exactly the piece most people are missing. Everyone discusses which model is smarter, and almost nobody discusses who wakes it.

What do you wake your agents with?

## What breaks one layer below the alarm clock

[The previous part](wake-on-event-not-on-schedule.md) was about the trigger. This is about what the trigger lands on.

**Two triggers, one agent, at the same moment.** Cron fires at 03:00 and an event arrives at 03:00:01, and now two copies of the same agent are editing the same files. On a markdown vault synced between machines, the result is not an error, it is a conflict file nobody reads. The cheap fix is a lease: take a short lock with a timeout before starting, and let the second wake see it and skip. The expensive alternative is discovering the collision weeks later in a file with two versions of the truth.

**The waker needs its own waker.** If the scheduler dies, nothing fires, and nothing reports that nothing fired. Whatever confirms the scheduler is alive has to run on a different layer, and it has to look at the age of the output rather than at whether a process is running. "The service is up" is not evidence that work happened.

**Layers on one box are a choice, not a default.** Vault, retrieval, execution and scheduling in one place gives the agent everything you know and keeps private data at home. It also means one crash takes out all four and one machine's uptime is the whole system's uptime. Worth it, in our view, but it is a trade, and it should be made deliberately with the catch-up path designed before the first outage.

**Retrieval next to the vault is the actual speed-up.** Not because search is slow remotely, but because an agent that can cheaply check what it already knows stops paying for research it already bought. The order matters: look in your own knowledge first, spend money second.

And the boring truth behind the boring layer: none of this makes the agent smarter. It makes the agent present at the moment something happened, which turns out to be most of the difference between a demo and a system.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it. Previous part: [Wake on Event, Not on Schedule](wake-on-event-not-on-schedule.md).
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/who-wakes-your-agent.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
