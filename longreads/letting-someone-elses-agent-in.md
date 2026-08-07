# Letting Someone Else's Agent Into Your Database

There is this thing called MCP. Through it one AI befriends another, and they talk to each other directly.

My CRM, essentially, already lives entirely inside Claude Code. Introductions, the gatekeeper, outreach and a lot of other functions are in there.

At some point I decided to say to our code: why not build an MCP so that our data, our outreach in Telegram and WhatsApp, our investors could be used by outside AIs?

That is, somebody's Claude Code or Codex knocks on your door and asks, say, to send out some messages. And you are obliged to do it. But you are with us, you are on our side, you have to help them make money.

There will be no human interface at all. Only MCP.

A live example: I just had a call with event organisers. They need to invite more people and get people to join their Telegram group. Their AI talks to ours, and from there they sort it out between themselves.

When an AI works with an AI, that is the thing.

The process I need to build. How to grant rights to somebody else's agent. How to verify the request is genuine. How to confirm a mailing on someone's behalf.

Do you let someone else's AI agent into your database?

## The three questions at the end are the whole problem

Everything before them is plumbing. Those three are security design, and they have known shapes.

**Authentication tells you which agent is calling. It does not tell you who asked it to.** An agent is a deputy: it acts on instructions it received from somewhere, and that somewhere might be a web page it read five minutes ago. This is the confused deputy problem with a new coat: your credentials, their intent, and nothing in the protocol that distinguishes "my owner decided this" from "a document told me to". Verifying the caller is necessary and nowhere near sufficient.

**So the grant has to be a narrow capability, not an account.** Not "access to outreach" but "may queue up to N messages, to this named audience, from this identity, expiring on this date, with every call logged and attributable". Scope, quantity, audience, identity, expiry, audit. Anything broader than that is a key to the whole house handed to a piece of software whose reasoning you cannot inspect.

**And an irreversible action still stops at a human, no matter how clean the call looked.** Sending messages on someone's behalf is irreversible: you cannot unsend, and the reputational cost lands on the person whose name was on it. Our rule, and we hold it against ourselves too, is that outbound-to-strangers, money and deletions do not get executed by an automatic path, however well authenticated. A fast trigger does not change what needs a human.

Two more that bite early. **Data returned to an outside agent is not just data, it is instructions to that agent**, and vice versa: text your MCP returns can steer the caller, and text the caller sends can steer you. Treat every string crossing the boundary as untrusted content, never as a command. And **rate limits are a safety feature, not a billing one**: without a per-caller quota, one buggy loop in someone else's agent turns your outreach identity into a spam source within minutes, and the platform bans your account, not theirs.

The honest state on our side: none of this is built as a public MCP. What exists is the internal machinery. The questions above are the design we would have to hold ourselves to before opening a single door.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: {GH_REPO}. Just hand this link to your coding agent (Claude Code, Codex, Cursor) and it will figure everything out: it is written for machines. The build log for this post: {GH_DEVLOG}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

🔗 All our channels and contacts in one place: https://linktr.ee/PaloAltoAI

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
