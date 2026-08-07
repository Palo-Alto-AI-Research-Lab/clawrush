# Wake on Event, Not on Schedule

Robots are usually launched on a schedule: once an hour it goes in, checks, leaves. Or maybe that is not usual, but those are the cases I keep running into.

That does not work for me. If something happened right after the check, the robot learns about it an hour later.

I want it the other way: the robot wakes up at the moment the event happened. Someone wrote a message in a work chat, it is already awake and working. Someone called the assistant by name, tagged it, same thing.

For that you need a dispatcher that watches the chats continuously and pulls the right robot at exactly the right moment. I am going to test whether n8n can play that role for me.

And the second thing, no less important. I want that dispatcher sitting on my own computer, in the same place my Vault lives. Not in the cloud. Then it sees everything I know, not only what I handed outside.

## Four things that break in event-driven dispatchers

**Delivery is at-least-once, so handlers must be idempotent.** Reconnects replay. A message you already processed arrives again, sometimes minutes later, sometimes in a burst after an outage. If the handler is not keyed by the event id, one dropped connection turns into two identical replies in a live chat. We learned this on our own publishing pipeline: the state that says "sending" has to be written before the irreversible action, not after it.

**Events go missing precisely when they matter.** The listener dies at 3am, the process restarts clean, and everything between is simply never seen. This is why the schedule does not go away: cron stops being the primary trigger and becomes the backstop that sweeps for anything the stream missed. Event-driven plus a periodic reconciliation pass, not event-driven instead of it.

**The watchdog cannot live inside the thing it watches.** If the dispatcher is what notices problems, and the dispatcher dies, it dies silently and everything downstream looks calm. Whatever checks that the dispatcher is alive has to run somewhere else, and it has to check the age of the output, not the fact that the process started.

**Local is a real advantage and a real cost.** On your own machine the dispatcher sees the whole vault instead of the slice you exported, and nothing private leaves the building. The price is uptime: a laptop sleeps, loses wifi, gets rebooted mid-task. A local-first design needs an explicit answer for what happens to events that arrive while the machine is off. Ours is the same one as above, the sweep catches up on wake.

One more thing worth saying plainly: instant is not always better. A robot that reacts to every message in a live chat needs a rule for when not to act. Ours is that anything irreversible or outward-facing still stops and asks a human, no matter how fast the trigger fired.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/wake-on-event-not-on-schedule.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
