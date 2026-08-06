# Dev-log: rebuilding the chain that carried this post

2026-08-06. This post has no code in it. It is a founder thinking out loud about money and influence. The build log is worth keeping anyway, because the pipeline that moved it from a Facebook wall to this repository was rebuilt from scratch on the same day, and four of its failure modes are the kind that stay invisible until they publish something wrong.

## The chain
One post, five stops, strict order: Facebook (human posts by hand) then GitHub longread and dev-log, then two Telegram channels carrying the GitHub links, then two Telegram chats carrying teasers that link to the channel posts, then Medium (human posts by hand). Each step reads the URL produced by the step before it. Links are written as placeholders and substituted at publish time, and an unresolved placeholder is a hard refusal, so a post containing the literal string of an unfilled link cannot physically leave the machine.

## Problem: an address that looks like yours is not yours
**Problem.** Two of the four teaser destinations in the original spec were public chats whose names were nearly identical to ours.
**Cause.** They were identified by name. Nobody asked what rights the sending account actually held there.
**Solution.** Before an address enters the config, query the participant record for the sending account. The answer was unambiguous: creator in two of our targets, admin in two others, and not even a participant in the two look-alikes. They were removed. A test now fails if either handle returns to the config, because a typo that publishes a founder's post into a stranger's chat does not announce itself.

## Problem: a successful push does not prove a working link
**Problem.** The channel posts carry GitHub URLs. If a file lands on the wrong branch or path, the push still reports success and the channel post links to a 404 that everyone reads.
**Cause.** Treating the write call's exit status as evidence about the resulting artifact.
**Solution.** After writing, read the file back from the target branch through the API. Only a successful read-back marks the step published and unlocks the channel step.

## Problem: one dropped connection becomes two identical posts
**Problem.** If the connection dies between sending a Telegram message and recording it, a naive retry publishes the same post twice.
**Cause.** State written after the irreversible action instead of before it.
**Solution.** The state `sending` is written before the send. On the next run that state is neither a green light nor a silent retry: it is a stop with instructions to look at the channel with human eyes, then either record the message that did go out or force a repeat. Four destinations carry four independent states, so a failure on one never re-fires the other three.

## Problem: approval that no longer describes the text
**Problem.** A human approves a teaser, someone edits a word, the approval still reads as valid.
**Cause.** Approval stored as a name and a timestamp rather than as a statement about specific bytes.
**Solution.** Approval is stored against the hash of the exact text with links already substituted. Any edit invalidates it, and the text is shown again before anything is published.

## Verification
Seventeen gate tests, all green, proven able to go red by mutation: removing the placeholder check, the approval hash comparison, or the stop flag each turns the suite red. Both live rails were exercised end to end on 2026-08-06, a file written to this repository, read back, and deleted again, and a Telegram message sent to Saved Messages only. Nothing was published to any channel during the build.

The full story, for humans: {GH_LONGREAD}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
