# My Whole YouTube History Goes Into the Vault

I worked out which other integration I need to add to my Obsidian.

I absolutely need to move my entire YouTube history in there, all the years of it. And my browser history too.

Then process all that history through RAG, so I can look at what I watched in different periods, what music I listened to and when.

Out of that comes what I actually like. And an understanding of who to learn from.

It is exactly the way to pull out all those AI engineers I watch on YouTube and want to learn from.

## Two rules we already learned the hard way

If you build this, two things will bite you, and both are cheap to prevent.

**Watch history is exposure, not belief.** What a person watched is evidence that they were exposed to an idea, not that they hold it. Dump a decade of watch history straight into a knowledge base and the retrieval layer starts answering questions about your opinions with other people's opinions, in their voice, with your name on it. Our rule: everything harvested this way carries the real author, which is the creator, not the owner of the account. The signal we want is "who to learn from", and that signal survives the distinction. The false signal, "here is what I think", does not.

**Liked-only, and quarantined first.** Full watch history is mostly noise: autoplay, background music, things opened and abandoned, things watched to argue with. We take the explicit signal, the likes, and even those land in a quarantine area outside the main retrieval index until they prove useful. A knowledge base that eats everything stops being a knowledge base and becomes a log.

There is a third boundary, less technical. Browser and watch history is the most intimate dataset a person owns, more revealing than mail. Ours stays local, on our own machines, never leaves for an external service, and never lands in anything that gets shared. That is not a feature we advertise. It is the condition under which this is buildable at all.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
