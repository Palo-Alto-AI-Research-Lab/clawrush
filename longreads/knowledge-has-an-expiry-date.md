# Knowledge Has an Expiry Date

A thought I want to build into the system.

I want to point AI at every blogger digging into AI, in Russian and in English, on YouTube and in Telegram. Let their content be parsed regularly, and I look at it: maybe something from there can go into my knowledge, into my Obsidian.

But not everything should go in. You have to separate the advertising noise: NVIDIA earned another pile of money, Anthropic shipped a new model, and everything else in that vein. If we see content that will let us code better, that goes in. The main thing is to put in quality.

And then the most important part. My Claude Code, every time before it searches for anything, must first look at whether it already has knowledge in the vault on that topic.

Because knowledge is expensive. And knowledge is worth collecting.

But any knowledge goes stale. We need to use it while it is still current.

I used to sell processors and memory. Processors and memory go obsolete very fast: what is current now is junk in six months. Electronics is the same, televisions, hard drives, graphics cards. And knowledge about them lives exactly as long.

So every piece of knowledge should have a date of relevance. And the system should understand which knowledge is due for a refresh.

## The part we measured on ourselves today

This is not a hypothetical failure mode. Today one of our own written rules expired without anyone noticing, and it cost about an hour.

A configuration file in our fleet carries a rule saying that a particular publication ledger has exactly one writer, a specific machine, and that every other machine must send that machine a task instead of writing the file itself. The rule was read and obeyed correctly. It was also no longer true: the machine named in the rule does not have that component installed at all any more. Two separate machines searched their own disks and answered, in writing, that the file is not there.

Nothing was broken. No test failed. No alarm fired. An obedient reader followed a rule that had quietly expired, and the work went to a node that could not perform it.

That is the whole argument for a date of relevance, in one incident. A rule, a benchmark, a price, a verdict that some integration is dead, all of them are knowledge, and all of them rot at their own speed. The dangerous ones are not the obviously old ones. They are the ones that still read as authoritative.

Which is why the verdict "this thing is dead" now expires here after thirty days unless it carries a date and a stated way to re-check it. Without those two, it is not knowledge. It is a rumour with good posture.

Let us develop this topic further.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
