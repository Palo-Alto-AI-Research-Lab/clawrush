# Make Your AI Admit It Failed

I dictate tasks to my AI and realise I am repeating myself. Again I am saying that if it stumbles on something, for example it searches for files on drive C when everything is on drive E and C only holds scripts and skills, we need some way to debug that.

I need it to not be shy about saying what is not working out: where it looked, where it got nothing at all.

The main thing is that it debugs itself.

I made this a rule that sits in the permanent instructions and loads into every session:
- stumbled, do not hide it: say what failed, where you searched, which paths you checked, what you expected, what you found, at which step you fell;
- empty from one place does not yet mean "nowhere" — walk all of them;
- the cause of a failure is a claim exactly like the conclusion: either you proved it, with what, or you honestly write "hypothesis";
- and separately: if the conclusion suits me because it takes work off my plate, check it harder, not softer.

Between "it would be nice if it admitted things" and "it is obliged to admit them, otherwise that is a defect" — the whole difference lives in that gap.

So far most of my errors are exactly in its search processes. When the material definitely exists, and the AI does not find it and says there is nothing.

But I have complained to you about that already.

Does your AI admit it when something did not work?

## The rule works, and here is what it caught today

The honest way to write about a rule like this is not to praise it. It is to list the times it fired on us, today, in the pipeline that published this post.

**A false "no", caught by a guard rather than by me.** Writing "there is no trace of it" while meaning "no such line inside this file" reads to a human as "that file does not exist". The fix that holds is mechanical, not attitudinal: name what exactly is missing and where you looked, and run an existence check before the word "no" leaves your mouth. Same class as the drive C versus drive E problem in the post: one place searched, conclusion drawn about all places.

**A written rule that had quietly stopped being true, obeyed perfectly.** Our config says a certain ledger has exactly one writer and everyone else must send it a task. That rule was read and followed correctly, and it cost about an hour, because the machine named in it does not have that component any more. Nothing errored. An obedient reader following an expired rule looks exactly like an obedient reader following a live one.

**A gate that watched one door.** The check that refuses to publish text with unresolved link placeholders covered messages going to chats and not files going to the repository. Twenty-six files sat publicly for a day with literal braces in the footer. The gate you did not write is precisely where it leaks.

The fourth line of his rule is the one that actually costs discipline: **if the conclusion suits you, verify harder.** A conclusion of "there is nothing there" ends the search, and ending the search is comfortable. Errors in your own favour generate no friction, which is exactly why they survive. In our case it was cheap to check and expensive to skip, both times.

And a note on the phrasing at the end of the post, which is the load-bearing part: "it would be nice" produces nothing. "Otherwise it is a defect" produces a test. Everything above only became visible because something mechanical was watching, not because anyone felt more honest that day.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/make-your-ai-admit-it-failed.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
