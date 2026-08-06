# Watched, Not Subscribed

More on analysing YouTube watch history and building a system out of it. [The first part is here.](my-youtube-history-into-the-vault.md)

The order goes like this.

Find the authors I am most interested in. Not by subscriptions, but by what I actually watched.

Then continuously monitor those authors for new content.

The content can be all sorts: connected to coding and not connected to it. Coding here means, for example, working with data, data science, data analytics and so on.

Hook up an LLM or some other transcriber to all the videos I have already watched. And the ones not yet watched, which we also want to pull in as knowledge, download separately.

Lay out all the authors and everything interesting into the shared knowledge base. It matters to cross-link everything and to understand whether we have any alpha, any real use, out of all the content we have watched and will watch.

Pull out the topics we have worked on and keep working on. Then for each topic look for overlaps: what have I already watched and read on this topic.

And all of this needs to happen regularly, on an ongoing basis.

Do you do the same?

## Four things that decide whether this works

**Subscriptions are a stale intention. Watch time is behaviour.** A subscription list is a snapshot of who you meant to follow, sometimes years ago. Rewatching is the strongest single signal in this dataset, stronger than a like: nobody rewatches a video by accident.

**Transcription is cheap, judgement is not.** The pattern that survives contact with volume is a cheap deterministic detector followed by an expensive judge. Transcribe locally on your own GPU, filter and deduplicate with plain code, and spend model tokens only on the shortlist. Sending everything to a model scales cost linearly with your history and produces summaries nobody reads.

**Alpha is a verdict, not a tag.** "Is there anything useful here" has to end in one of three states: taken, with a note on what changed; already known, with a link to where we knew it; noise. A pile marked "interesting" is a pile.

**Regular means a robot, and a robot means an owner.** Anything that needs doing constantly and is done by a human gets done for two weeks. But a routine with no named consumer is worse than no routine: it produces output nobody reads, and its silence looks exactly like health. Name who reads the output before scheduling the job.

One boundary from the first part still applies: watching is exposure, not belief, so everything harvested carries the creator as its real author. The question this corpus answers well is who to learn from. It answers "what do I think" badly, and confidently.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it. Part one: [My Whole YouTube History Goes Into the Vault](my-youtube-history-into-the-vault.md).
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
