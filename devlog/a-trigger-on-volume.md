# Dev-log: the return contract is the hard half of delegation

Handing work to an external model is two halves. The outbound half, a prompt with data and context, is easy and everyone builds it. The inbound half is where delegation quietly stops paying for itself.

## Problem: the answer comes back as prose
**Problem.** An external research answer arrives as several pages of well-written text. A human then reads it, decides what mattered, and retypes that into the system.
**Cause.** The request asked a question and did not specify a return shape.
**Solution.** The package carries an explicit return contract: named fields, the format, sources with dates, and an instruction to say "not verified" instead of filling a gap. The test is simple: can the answer be ingested without a human deciding what it meant. If not, the contract is missing.

## Problem: the outside model re-derives what we already settled
**Problem.** An external answer confidently contradicts a decision made weeks ago, and does it with better prose than the original.
**Cause.** The package carried the question but not the relevant slice of existing knowledge.
**Solution.** Data, then context, then prompt. The context slice is the recall output from the previous rule in this thread: if recall found something, it goes into the package, and the outside model is asked to argue with it explicitly rather than start from nothing.

## Problem: a threshold made of vibes
**Problem.** "If the task is large, delegate" cannot be implemented, because large is not a measurement.
**Cause.** The trigger was written as a judgement rather than as a countable quantity.
**Solution today: none, and that is the honest answer.** Candidate measurements exist, number of sources to read, size of context the task drags in, count of independent claims needing verification, and none of them has been calibrated against real tasks here. The rule currently fires when a human notices. Writing "the agent decides automatically" would describe a system we do not have.

## Problem: delegated research that never lands
**Problem.** A request is sent, answered, filed, and never used. It looks complete in every dashboard.
**Cause.** The lifecycle ended at "answer received".
**Solution.** Each request names its consumer at creation and closes as applied, with what changed, or parked, with why. Both are endings; silence is not.

The full story, for humans: https://github.com/tonydzi/clawrush/blob/main/longreads/a-trigger-on-volume.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
