# Dev-log: the publishing chain that carried this post

This is the build log of the pipeline described in the post above, written from inside it. Numbers are counted from the case journals on 2026-08-07: 20 cases, 138 recorded publications, 45 gate tests green.

## The shape
One source post becomes seven artifacts in a fixed order: longread and dev-log in this repository, a full post in each of two Telegram channels, a teaser in the English chat, a short version for X, and a Medium file a human publishes by hand. Every destination has its own state, so a failure on one never re-fires the others.

## Problem: the order is a dependency graph pretending to be a checklist
**Problem.** The channel post contains the GitHub link. The teaser contains the channel link. Run them in the wrong order and you publish a post that points at nothing.
**Solution.** Links live in the text as named placeholders and are substituted at publish time from the state of earlier steps. An unresolved placeholder is a hard refusal, not a warning. A post containing the literal string of an unfilled link cannot physically leave.

## Problem: the gate that only watched one door
**Problem.** Twenty-six files sat in the public repository for a day with literal `{...}` placeholders in the footer.
**Cause.** The placeholder check ran on text going to chat destinations. Files pushed to the repository took a different path and were never checked. Additionally, a longread references its dev-log, whose URL does not exist until the dev-log is pushed, so a single pass cannot resolve everything by construction.
**Solution.** A second pass over the already-pushed files once both URLs exist, plus a check that no placeholder survived. Fixed retroactively for all 26 files, verified by reading them back through the API.

## Problem: configuration copied at creation time
**Problem.** Two incidents in one day. A destination was paused, and a case created before the pause did not see it, so a message went out against an explicit instruction. Separately, the repository changed owner; GitHub silently redirects reads and refuses writes with 307, and every existing case still held the old owner.
**Cause.** The case snapshotted config at creation. A snapshot cannot learn that the world changed.
**Solution.** Destinations and repository are read live at the moment of the action; the snapshot in the journal is history. Both incidents now have tests that go red against the old code.

## Problem: a pipeline with no reject path
**Problem.** Everything on the wall becomes seven artifacts, including things that should not be published at all.
**Solution.** Explicit skips at any granularity, each requiring a stated reason and a name: whole post, GitHub, dev-log alone, Medium. Of 20 cases: one skipped entirely, one published without GitHub, one with a longread but no dev-log. Silence and refusal look identical afterwards unless the refusal is written down.

## What is verified and what is not
Verified: the tests go red on broken code, proven by mutation on the placeholder check, the approval hash, the stop flag and the second pass. Both live rails were exercised end to end.
Not verified: any claim that this improves SEO or GEO retrieval. We have published a lot and measured nothing on that axis yet, and until there is a number, there is no claim.

The full story, for humans: {GH_LONGREAD}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
