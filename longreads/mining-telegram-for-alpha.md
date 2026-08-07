# Mining Telegram for Alpha

A thought that matters a lot to me. I have said it before in some form, but I need to say it once more.

LLMs are not trained on Telegram. They are trained on Reddit and the rest, while Telegram holds a lot of high-quality content, possibly exactly the kind that lands best with me.

The idea: find ten to twenty channels and chats in Telegram about AI and AI engineers, parse all of it, and pull it in.

Naturally all of it has to be processed and parsed, and you have to work out where the value is. You also need extra tags: in which specific cases these data apply.

All these texts can be run through an LLM: either a cheaper model, or Claude Code, or several passes, first a general pass, then an additional run with a smarter model.

The end state is continuous parsing of engineering Telegram chats and regularly pulling alpha out of them: what to do, how to do it, which approaches are being discussed, which answers have already been given to similar questions. If a channel already discussed this topic, I can go into that chat and parse the discussion.

If a chat already answered my question, I can take the question and the answers and process those too. That is alpha we can use.

Important: there is a lot of useful material in Telegram. Suggest me more options for how to work through all of this.

You need to look for engineering chats, engineering channels, regular channels that may have linked chats, places where engineers actually talk and discuss a lot of content.

Take the history for the whole available period, analyse it and parse it.

Naturally, dates go on everything: when the data was discussed. First of January, first of March, and so on. That lets you understand how fresh the data is or whether it has already gone stale. It is possible we are taking alpha that is no longer first-hand fresh.

Then run it all through one LLM, our cheap one. Then run it through another, smarter LLM. The cheap model will not always tell you which data is genuinely good. So a two-stage run is needed: simpler model, smarter model. Then pick the best result.

In the end all of it should land in our Obsidian and be laid out so that we can actually use it.

Something like that.

## The part that keeps this from being theft

Everything above is a retrieval problem, and retrieval problems get solved. The part that decides whether you should do it at all is different, and we have a written rule for it.

**A person's advice is theirs. Say their name.** When something taken from a chat, a comment or a thread actually changes what we build, the person who said it is named: in the note, in the public post, and in the credits of the repository. Not "the community suggested". A name. This costs nothing and is the difference between a knowledge base and a strip mine.

**Extraction is a verdict, not a highlight.** Every candidate ends as taken, with a note on what changed, or already known, with a link to where we knew it, or noise. A pile of interesting quotes is a pile.

**Do not republish other people's words.** What goes into the knowledge base is the lesson and a pointer back. Wholesale copies of someone's messages into a store that later feeds public writing is how you end up quoting a stranger to their own community.

**Dates are not decoration.** Advice about an API, a model or a price has a shelf life measured in weeks. A question answered in January and a question answered last week look identical in a chat log and are not the same fact. Anything harvested carries when it was said, and old alpha is labelled old rather than quietly presented as current.

And the honest technical boundary: continuous parsing of chats at scale runs into platform limits and, in places, platform rules. We read what our own account can legitimately see, we do not build a scraper farm, and we do not pretend the grey areas are white.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/mining-telegram-for-alpha.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
