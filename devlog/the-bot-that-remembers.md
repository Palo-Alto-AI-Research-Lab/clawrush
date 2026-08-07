# Dev-log: reading task state out of a human chat

Extracting commitments from unstructured conversation is the easy-looking half. The hard half is deciding what counts as done, and not becoming the thing people mute.

## Problem: counting handoffs instead of state changes
**Problem.** A tracker that watches messages reports steady activity while nothing finishes.
**Cause.** The event it recorded was "passed along", which is cheap and frequent, instead of "state changed", which is rare and expensive.
**Measurement.** On one of our internal pipelines a courier robot logged 29,341 handoffs and zero completions over two weeks, and the dashboard looked healthy the entire time.
**Solution.** The unit is the state transition with evidence attached: taken by whom, blocked on what, done with a link. A message is a hint that a transition may have happened, not the transition itself.

## Problem: silence parsed as an answer
**Problem.** No reply gets interpreted, usually as "in progress", occasionally as "done".
**Cause.** The model was asked to classify a conversation and will always return a class.
**Solution.** Unknown is a valid, first-class state. The bot asks once, explicitly, names the item, and if there is still no answer, the item stays unknown and visible rather than being quietly resolved. Guessing here is worse than not tracking, because a wrong "done" removes the item from everyone's view.

## Problem: the reminder that gets muted
**Problem.** Identical nudges repeat until the human filters the bot.
**Cause.** Retry logic was copied from network code, where repeating the same packet is correct.
**Solution.** Escalate rather than repeat: a quiet mention, then a direct question naming the blocker, then a human above, and only for genuinely time-critical items. Each step is worded differently, and the ladder is capped. Also worth having: a rule that the bot never nudges outside working hours, because a 2am reminder trains people to turn off notifications entirely.

## Problem: it sees a room full of people
**Problem.** A bot in a working chat reads personal asides, complaints and half-formed plans along with the tasks.
**Cause.** Ingest was scoped to a channel, not to a purpose.
**Solution.** Store the commitment and its state, not a portrait of the person who made it. Same rule as the group-registry work in this repo: keep the edge, not the dossier. It also keeps the bot useful, because a tracker full of mood data is not a tracker.

## The design goal, stated plainly
Not accountability to the bot. The bot exists so the list lives somewhere other than a human head. Once it feels like supervision, people start managing the bot instead of the work, and the tracker becomes another thing to maintain.

The full story, for humans: https://github.com/tonydzi/clawrush/blob/main/longreads/the-bot-that-remembers.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
