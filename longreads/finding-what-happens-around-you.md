# Finding What Actually Happens Around You

Two tasks I gave my AI about not missing the interesting things around me.

**First. The chats of the location where I live.**

It should go through all my Telegram chats connected to the place where I live and to entertainment in it. I have a lot of chats on that theme.

By the way, it seems to me that all the chats we have, and what gets discussed in them, would be worth putting into our RAG storage. Then it will be easier for us to find where exactly the thing we need is discussed. You immediately see: these chats talk about one thing, those about another.

What is needed:
- find all the chats where the topic is discussed;
- go into them once a week;
- look for all the events;
- compile a list of interesting events for the coming week.

**Second. Travelling around Europe.**

When we were getting ready for a trip, I gave my AI the same task, only wider.

What needs doing:
- run deep research on the region;
- find all the local venues where events get published;
- find local Telegram groups in Russian and Ukrainian;
- pull exhaustive information out of them about what is going to happen.

How do you find out what interesting things are happening around you?

## Four things that break in event extraction

**Dates are the hard part, not the search.** "Next Saturday" written on a Thursday, "the 5th" with no month, "tomorrow at 7" posted a year ago and still sitting in the archive. Every extracted event needs an absolute datetime and a timezone, resolved against the moment the message was written, not the moment you read it. Anything that cannot be resolved goes out as unknown rather than as a guess, because a confident wrong date sends a person to an empty room.

**The same event appears in five chats, worded five ways.** Deduplicate on the event, not on the text: venue plus start time is a decent key, and near-identical titles cluster. Keep the earliest post as the origin and the rest as corroboration. Five mentions mean the event is popular, not that it is real, and cancellations rarely get posted with the same enthusiasm as announcements.

**Location is ambiguous in exactly the way that hurts.** Cities repeat across countries, venues repeat across cities, and a chat about a place is not the same as a chat in that place. Bind extraction to a resolved location, and when it cannot be resolved, say so instead of assuming the nearest match.

**This answer expires faster than any other in the system.** A list of events for the coming week is worthless on the eighth day and actively misleading on the tenth. Same rule as everywhere else here: the fact carries its date, and stale is labelled stale rather than quietly served as current.

And a note on the RAG idea in the middle of the post, which is the most useful line in it: indexing your own chats is less about search and more about knowing which room discusses what. That map is the thing you cannot buy, and it is why the group registry and this task are the same project seen from two ends.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
