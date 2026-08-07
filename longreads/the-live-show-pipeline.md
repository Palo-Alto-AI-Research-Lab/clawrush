# The Live Show Pipeline

Americans know how to do show business. Out of any thing where something is happening, they make a show: series, documentaries, music, the heat of it.

I want the same, only about what I do myself.

I use coding tools a lot, Claude Code, Codex, Cursor, GitHub, Obsidian and so on, and I have now started showing that publicly.

Here is how I see it:
- teasers on Twitter and Telegram, including from different people;
- from the teaser a person goes and reads a medium-sized post, on Facebook for example;
- from there to the longread, on my site, in the Telegram channel, on GitHub, on Medium, and if the material is research-grade, then arXiv and so on;
- and everything is connected by links, from the shortest teaser to the longest explanation.

Why all this. I want to be indexed in SEO and in GEO. SEO is when a search engine finds you, GEO is when AI search finds you. I want my knowledge indexed as widely as possible, and for the community of engineers who also love doing this to reach out to me.

But the main thing is for it to genuinely be the way Americans like it. A live show that I host. Every day a post comes out, and people understand what is happening with me right now and get interested in what comes next.

Any more ideas on how to organise all of this properly?

## What this looks like when it is actually running

This post travelled through the pipeline it describes. That is not a metaphor, so here are the numbers, counted from the journal rather than estimated.

Twenty posts have gone through the chain in the last two days. One Facebook post becomes, in order: a longread and a dev-log in this repository, a full post in the English channel and in the Russian one, a teaser in the English chat, a short version for X, and a file for Medium that a human publishes by hand. That is 138 publications so far across all destinations, every one of them recorded with its link.

Four things we learned running it, all of which cost something first.

**The order is a dependency chain, not a preference.** The channel post carries the GitHub link, so GitHub goes first. The teaser carries the channel link, so the channel goes first. Get the order wrong and you publish a post pointing at nothing. Links are written as placeholders and substituted at publish time; an unresolved placeholder is a hard refusal.

**And that refusal has to cover every destination, not the loud one.** Ours checked the text going into channels and not the text going into the repository, so twenty-six files sat publicly for a day with literal placeholder braces in the footer. Found and fixed today. The gate you did not write is exactly where it leaks.

**Config read at creation time goes stale.** Two separate incidents in one day: a paused destination that a case created earlier could not see, and a repository that moved owner while cases still held the old one. Same class. Configuration is read at the moment of the action, and the copy in the journal is history, not truth.

**Not every post belongs everywhere.** Of twenty posts, one was skipped entirely, one went to the channels without GitHub, one got a longread but no dev-log. Each skip carries a written reason and a name. A pipeline that only knows how to say yes is a funnel, and silence looks identical to forgetting unless the "no" is recorded.

On the GEO part, one honest note: writing for AI search is not a trick layer on top. What actually helps is what also helps a human, which is a claim with a date, a number with a source, and a stated boundary between what is built and what is planned. We have no measurement yet on whether this improves retrieval, and we will not claim one until we do.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/the-live-show-pipeline.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
