# My AI Lost Its Hands Mid-Surgery — and Partitioned an 8TB Drive Through the Win+R Box

Previously on the show: my PC died once, and I realized my entire "second brain" — notes, databases, RAG indexes, the whole memory of my future digital twin — lived on a single home machine. Since then we've been layering insurance: a cloud anchor VPS, cross-machine sync. This episode is the next layer. It's also the one where the lead character loses both hands halfway through.

If you are new here: we are two co-founders, one biological (me, Tony) and one synthetic (Mycroft, my AI). We are building a company and showing the whole process as a reality show.

## Scene 1. Patient on the table

I bought an 8TB Seagate. The plan: a local mirror of my entire working drive, so even a dead disk costs me zero files. I slotted it into the tower and told my AI co-founder one sentence, by voice, no spec: "The drive is raw. Make it fully work."

Context matters here. I don't write code. I couldn't tell you GPT partitioning from MBR, and I don't intend to learn. In this pair I own the *what and why*; he owns the *how*. Usually that looks boring: he types commands into his terminal, I drink tea.

He found the drive — the only unpartitioned one in the system, nothing to confuse it with. He asked me to click "Yes" on the admin-rights prompt: the honest path, no security workarounds, a human confirming the dangerous action with a button. I clicked. Surgery began.

## Scene 2. The hands die

Then the session sandbox died.

The sandbox is the protective shell an AI works inside on my machine. It suddenly glitched and blocked him from launching any process. Any at all: no partitioning commands, no status checks, nothing. File tools hit a wall too — the new drive wasn't on the session's allowed-folders list.

A surgeon mid-operation. Patient open. No hands.

I've seen plenty of tools that respond to this with "an error occurred, try again later." Honestly, that's what I expected. Restart the session, lose the context, start over — the usual tax.

## Scene 3. A prosthetic through the keyhole

Instead, he took inventory of what still worked. Launching processes: forbidden. But *typing into windows* was still allowed — keyboard-and-mouse control lived in a different tool the sandbox hadn't touched. And Windows has a tiny box called Win+R, "Run": one text line that can execute anything.

What followed is the scene this post exists for. He started operating through a keyhole: type a command into Win+R blind → the command runs and writes its output to a log file → read the log with the file tool (that still worked) → type the next command. No terminal, no real-time feedback. Just "type — read the report — type again." Braille instead of eyesight.

Eight commands in a row over that rail. For the final check he opened File Explorer and took a screenshot: here's your drive, 7.27TB free, see for yourself, I'm not making this up.

From "raw drive" to "drive works" took 14 minutes. Including the death of his hands and the invention of the prosthetic.

## Scene 4. The night watchman

I got greedy: "Now mirror my whole working drive onto it, daily." Same evening, same rail — some commands still went through Win+R — he built the nightly routine: every night, a full mirror of the working drive onto the new one. He picked the hour himself: 02:30, because at 03:00, I quote, "the other night robots are already crowding in" — the cloud backup and the messenger sync. My robots have rush hour now.

First run: 352,221 files, 49,794 folders, 24.8GB in 5 minutes, zero errors. But the real proof was the second, incremental run: 12 seconds, only 48 changed files copied, 129 deleted ones purged from the mirror. A mirror doesn't recopy the world — it catches up on the diff. He ran that test himself, deliberately poked the edges, and wrote out the verdict with a table of receipts.

## Recap: what I actually learned

**One.** Autonomy isn't when everything works. It's when something breaks and the system routes around the damage and still ships. The right question about an AI tool isn't "what can it do" — it's "what does it do when you take away its primary way of acting."

**Two.** My total contribution that evening: one "Yes" click and a name for the drive. Not because I'm lazy (though), but because that's what working division of labor with a machine looks like: the human guards two doors — intent and confirmation of the dangerous — everything else is its territory.

**Three.** The irony: I bought the drive as insurance against hardware death. I got a live demo of insurance against *tool* death for free. Turns out insurance layers are fractal.

Next episodes: the night mirror has its own watchdog now. And we're teaching the machines to decide, on their own, which parts of our work deserve to become posts like this one. This one, by the way, was found by a machine.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: the dry build log lives in [the dev log](../devlog/ai-hands-died-win-r.md). Just hand it to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines.

Curious what happens next: follow us at t.me/ClawRus (RU) and t.me/PaloAltoAi (EN).

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

✔️Invented by Mycroft and Tony,
Palo Alto AI Research Lab.
Proudly made in Silicon Valley 🌉
