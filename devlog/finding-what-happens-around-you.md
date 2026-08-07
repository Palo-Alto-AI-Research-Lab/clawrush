# Dev-log: extracting events from chat noise

Event extraction reads like a search problem and is mostly a temporal-resolution problem. Four failures, ordered by how much they cost a human who trusted the output.

## Problem: relative dates resolved against the wrong now
**Problem.** "Next Saturday", "the 5th", "tomorrow at 7" are resolved at read time instead of write time, and an archived message from last year produces an event next week.
**Cause.** The message text was passed to a model without the message timestamp as the anchor.
**Solution.** Resolve every relative expression against the posting time, output an absolute datetime with an explicit timezone, and treat anything unresolvable as unknown. A wrong date is worse than a missing one: it sends a person to an empty room and they stop trusting the whole feed.

## Problem: one event, five chats, five wordings
**Problem.** Naive extraction yields five items for one concert, and a weekly digest becomes unreadable.
**Cause.** Deduplication was attempted on message text.
**Solution.** Key on the event: normalised venue plus start time, with fuzzy title clustering on top. Keep the earliest post as origin, count the rest as corroboration. Note the asymmetry that matters here: announcements get reposted enthusiastically, cancellations almost never do, so corroboration count says nothing about whether the event still stands.

## Problem: place names are not identifiers
**Problem.** Cities repeat across countries, venues repeat across cities, and a chat *about* a place is not a chat *in* that place.
**Cause.** Location was treated as a string.
**Solution.** Bind extraction to a resolved location with coordinates or a stable place id, and when resolution fails, output unknown rather than the nearest match. Same principle as identity resolution for people in the group-registry work: an identifier is not an identity, and a plausible match is not a match.

## Problem: an output with a shelf life measured in days
**Problem.** A weekly event list is the fastest-rotting artifact in the system, and nothing in the pipeline treats it differently from a durable note.
**Cause.** Freshness was a property of the run, not of the record.
**Solution.** Every item carries the date it was extracted and the date it becomes irrelevant. Past its date it is labelled expired rather than being served as current. This is the sharpest instance of the rule the rest of this repo keeps repeating: a fact without a date is a rumour with good posture.

## The line worth stealing from the source post
Indexing your own chats is less about search than about knowing which room discusses what. That map cannot be bought, and it makes the difference between asking a model a question and asking the right room.

The full story, for humans: https://github.com/tonydzi/clawrush/blob/main/longreads/finding-what-happens-around-you.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
