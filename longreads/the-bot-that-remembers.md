# The Bot That Remembers So People Do Not Have To

One of my bots is connected to the chat with my assistants. And the first thing it needs is to understand how the work is actually structured and how it can be maximally, proactively useful to me.

What it should be able to do:
- take a task from me, understand it and break it into steps;
- help the assistants carry it out;
- read the results of the work straight from the correspondence: who took what, what got done, what is hanging;
- monitor what was forgotten and what is overdue;
- push so that things get finished;
- and so on.

The bot should not be too much of an angry policeman. It just needs to never forget anything itself, so that people do not forget either.

I think this is the most underrated role for AI in a team. A kind of micromanagement, but that pusher-reminder is definitely needed.

Who makes sure tasks do not get lost at your place?

## Four things that decide whether this bot is loved or muted

**"Delivered" is not "done", and that gap is the whole job.** Our own measurement on an internal pipeline: a courier robot reported "handed over" 29,341 times and "done" zero times, for two weeks, and nobody noticed, because handing over looks like progress. A reminder bot that tracks messages sent rather than states changed will produce exactly that number and call it health. Track the state change: taken, blocked, done, with evidence.

**Silence is ambiguous and must be treated as such.** No reply can mean done, forgotten, blocked, or on holiday. A bot that assumes any one of those is wrong most of the time. Ours asks once, explicitly, and marks the item unknown rather than guessing.

**Escalation, not repetition.** The fastest way to get muted is sending the same reminder five times. A ladder works: a quiet mention, then a direct question naming what is blocked, then, only if the item is genuinely time-critical, the person above. Every step needs a different sentence. Identical text repeated is spam, and spam gets filtered by humans exactly like it gets filtered by mail servers.

**It reads a room full of humans, so decide up front what it keeps.** A bot in a working chat sees everything: personal asides, complaints, half-formed plans. What we store is the commitment and its state, not a profile of the person who made it. Same line as everywhere else in this repo: an edge, not a dossier.

And the thing Tony gets right and most implementations get wrong: the goal is not to make people accountable to the bot. It is that the bot never forgets, so nobody has to hold the list in their head. The moment it starts feeling like a policeman, it stops working, because people begin managing the bot instead of the work.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/the-bot-that-remembers.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
