# Dev-log: cheap detector, expensive judge

Turning a watch history into a monitored feed of authors is mostly an economics problem. Four decisions, each one made after the naive version cost too much or produced too little.

## Problem: ranking authors by subscriptions
**Problem.** The subscription list ranks people you meant to follow, not people you learn from.
**Cause.** A subscription is an intention recorded once, sometimes years ago, and never revisited. It survives losing interest.
**Solution.** Rank by behaviour: watch count, completion, and above all rewatching. Nobody rewatches by accident, which makes it the strongest single signal in the dataset, stronger than a like.

## Problem: paying a model to read everything
**Problem.** "Transcribe and summarise all of it" scales cost linearly with history size and produces a wall of summaries nobody opens.
**Cause.** One expensive tool applied uniformly, with no cheap stage in front of it.
**Solution.** Cheap deterministic detector, expensive judge. Transcription runs locally on our own GPU, so it is free at the margin. Filtering, deduplication and topic matching are plain code. Model tokens are spent only on the shortlist that survives, and the judge reads a digest plus the target note, never the corpus.

## Problem: "interesting" is not a state
**Problem.** A knowledge base fills with items tagged interesting. Nothing is ever done with them, and nobody can tell which ones were already acted on.
**Cause.** The extraction had no terminal states, so everything stayed open forever.
**Solution.** Every candidate ends as taken, with a note on what changed, or already-known, with a link to where we knew it, or noise. Three endings, all cheap to write, and the pile stops growing.

## Problem: a routine whose silence looks like health
**Problem.** A nightly job that monitors authors and writes a digest is easy to schedule and easy to leave running unread for months.
**Cause.** Scheduling is a technical act; having a reader is an organisational one. The first happens, the second is assumed.
**Solution.** Name the consumer before creating the job, and measure consumption as a state change, not as an open. A routine nobody reads is worse than no routine: it burns compute and its silence is indistinguishable from everything being fine.

## Honest boundary
What runs today is the liked-only path with quarantine and creator attribution, from the previous entry. Ranking authors by rewatch, continuous monitoring of a chosen set, and per-topic overlap search are described here as design, not as shipped. The order in the post is the plan; this log is what we already know will bite.

The full story, for humans: {GH_LONGREAD}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
