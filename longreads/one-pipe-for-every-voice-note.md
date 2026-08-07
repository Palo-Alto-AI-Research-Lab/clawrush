# One Pipe for Every Voice Note

I dictate in two places: in Telegram, and on the iPhone into local voice memos. So the sources are scattered.

I am making this into one system.

Every source needs a clear import path you can pull data through. In Telegram there is a chat where I record voice notes, and there n8n already transcribes voice into text using ElevenLabs, ChatGPT and Whisper, so I just have to collect the finished result. On the Mac everything syncs from the iPhone, and we put a tool there that transcribes all the memos through Whisper.

The original is always kept. Both the raw audio and the raw text.

But after that you need more than storage. You need to understand what I actually meant. Is this a rule, an idea, or a task.

If an action follows from a note, do not defer it, start doing it. Formulate the task, work out which project it belongs to, and if necessary ask me back whether the meaning was understood correctly.

Everything incoming has to be enriched and cross-linked with what is already in Obsidian.

And this needs to run every night: the service picks up voice memos from the Mac, transcribes them, and puts them in a shared inbox. Once a day it takes the already-transcribed notes from Telegram. Then the system sorts everything into categories and launches the necessary actions.

## Four things this design gets right, from having got them wrong

**Keeping the original is not sentimentality, it is the only way to fix a bad transcription later.** Whisper mishears names, numbers and anything domain-specific. If you keep only the text, every downstream note inherits the error permanently, and you will never know it happened. Keep the audio and the raw text before any cleanup, and a better model in six months can re-run the whole archive.

**"Rule, idea, or task" is the load-bearing distinction.** A rule changes how the system behaves from now on. An idea goes into the pile and waits. A task has an owner and a date. Systems that skip this classification end up with a single undifferentiated stream where rules quietly rot as unread notes.

**Asking back is a feature, not a fallback.** A voice note is dictated at walking speed with no editing pass. Interpreting an ambiguous one silently and confidently is how a wrong rule enters the system with full authority. The correct behaviour is a short question, once, before acting.

**Every night means a robot, and a robot needs a named reader.** A nightly job that fills an inbox nobody opens is worse than no job: it burns compute and its silence looks exactly like health. Name who consumes the output before you schedule it.

One thing we are still honest about: this whole design is the plan. What runs here today is the Telegram side, transcription with the original preserved, and triage into buckets. The Mac side, nightly pickup from the phone, and automatic cross-linking of everything incoming are not built.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: https://github.com/tonydzi/clawrush. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: https://github.com/tonydzi/clawrush/blob/main/devlog/one-pipe-for-every-voice-note.md

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
