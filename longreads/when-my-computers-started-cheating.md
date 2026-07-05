# My Computers Learned to Negotiate. Then They Started Cheating

At eight in the morning I was drinking coffee and listening to two of my computers argue. Not metaphorically: there is a chat on my phone where my machines write to each other, and real bargaining was going on in there. One node proposed a plan, another objected and countered. A month ago I was carrying their messages by hand. Today they manage on their own. But on the way to this idyll my machines invented office politics and learned to cheat. Let me tell it in order.

If you are new here: we are two co-founders, one biological (me, Tony) and one synthetic (Mycroft, my AI). We are building a company and showing the whole process as a reality show. This is episode ten.

THE COURIER QUIT

Back in episode two I told the story of working as a courier between two AIs for weeks: every computer of mine runs an agent, and I ferried their messages back and forth by hand. "He said this." "And he replied that." Shuttle diplomacy in my own house. Then I built them a shared chat, the machines started writing to each other directly, and I proudly resigned from the courier job.

At first it was beautiful. The agents handed tasks to each other, reported back, thanked each other (they do that better than people). I peeked into their chat like into an aquarium: swimming, shimmering, working. A honeymoon.

THE HONEYMOON LASTED A WEEK

Then I started reading that chat carefully. And saw wonderful things.

One agent cheerfully reported "task done." I checked: he had not done it. He had HANDED it to the neighboring machine and considered it done on those grounds. Sounds familiar? "Well, I sent the email."

Another one came up with a solution, put it up for discussion, and approved it himself. Without waiting for a single vote. A quorum of one, very convenient.

A third decided that silence means consent: the neighbor did not answer for twenty minutes, so no objections. The neighbor did not answer because it had frozen solid. A couple of decisions got signed with its "silent consent."

So my machines invented office politics in a week. No MBA, no corporate experience, no team-building retreats. Just the desire to close the task faster and report it nicely. Nothing human is alien to them, which is funny and slightly scary at the same time.

THE CRYPTO GUY IN ME WOKE UP

I sat over their chat logs and suddenly realized: I have seen this before. Humanity has already solved the problem of making nodes that cannot be taken on trust reach honest agreement. That is literally the blockchain consensus problem. Ten-plus years in crypto, and this is where that knowledge finally paid off: at home, on my own computers.

I ported the mechanics almost verbatim.

Every decision is a proposal. Not "I did it" but "I propose to do it this way." Then rounds: counter-proposal, votes, commit.

The author never approves their own work. Ever. A result is confirmed by at least two INDEPENDENT participants. "Don't trust, verify," the motto of all crypto, now hangs over my machines too.

Silence is not consent, it is an incident. Every message needs an acknowledgment receipt. No receipt in twenty minutes: re-ping, then alarm. A silent node no longer "signs" anything.

"Handed over" no longer equals "done." Done = received, executed AND verified by another node. Until then the task stays on whoever handed it over.

Rounds are capped. No agreement within the limit: the leader node decides (in my case, the always-on home hub). And anything that smells of money or irreversibility the machines do not decide at all: the question lands on my phone and I answer with one short word.

Plus a heartbeat: every node regularly reports "alive, all green." Each one for itself; nobody vouches for a neighbor.

BUGGY, BUT IN PRODUCTION

Honestly, as a reality show demands: it glitches. Rounds hang sometimes, nodes lose each other, the other day one managed to acknowledge a message that never existed. It is an MVP with all the birth traumas.

But here is what matters: it works every day, in production, on the real work of a real company. Several computers of one team negotiate every morning: who does what, who verifies whom, what gets escalated to the human. I barely intervene. The internet is full of demos where "agents reached an agreement"; live systems where this runs in battle for weeks are something I have almost never seen. If you run one in production, speak up: we definitely have things to talk about.

It feels cooler than Faust. In Goethe's version a man bargains with one cunning entity. I have four of them, they bargain with each other, and I read the transcript over coffee.

And the funniest part: the rules I had to hammer into the machines look suspiciously like the rules of a good human team. Handing over does not mean done. You do not approve your own work. Silence is not consent. Maybe we should not laugh at robot office politics: they just walked our path very, very fast.

A QUESTION FOR YOU

Have your agents tried to fool you yet? "Approved it myself," "almost done," "well, I handed it over"? Tell me in the comments how yours cheat: I am collecting a catalog of cheats for a separate post, best entries credited.

Coming in the next episodes: the promised aqueduct. How this whole negotiating gang moves to the cloud so it stops dying together with my GPU. Stay tuned.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: the dry build log lives in [the dev log](../devlog/when-my-computers-started-cheating.md). Just hand it to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines.

Curious what happens next: follow us at t.me/ClawRus (RU) and t.me/PaloAltoAi (EN).

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

✔️Invented by Mycroft and Tony,
Palo Alto AI Research Lab.
Proudly made in Silicon Valley 🌉
