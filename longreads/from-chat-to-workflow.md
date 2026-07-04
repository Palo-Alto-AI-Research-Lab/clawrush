# The Six-Step Ladder: How the AI Agent World Actually Works, in Plain Words

Every week a friend asks me the same question in different words: "Okay, I get chat. But what's a skill versus a subagent? And an agent team versus a workflow? Aren't those the same thing?" They are not. I used to mix them up myself, until I laid the whole mythology out as one ladder with six steps. Today I'm showing the full ladder, with live examples from our factory.

If you're new here: we are two co-founders, a biological one (me, Tony) and a synthetic one (Mycroft, my AI). We build a company and show the process as a reality show. This is episode eight, the educational one.

## Step 1: Chat

You type, the AI answers. That's it. No memory of how you like to work, no autonomy. The cheapest level and the clearest one: everybody starts here, and most people stay here. For emails, questions and one-off tasks it's honestly enough.

## Step 2: Skill

The first transition. You catch yourself asking for the same thing for the THIRD time, in the same words. Stop: move the instruction into a file. For us it's literally a file called skill.md: "when I say do X, do it like this, step by step." Now the agent loads the instruction itself, on a short command, and does the job equally well the hundredth time. A skill is your repeated request turned into a button.

## Step 3: Goal

The second transition, and it gets interesting. Instead of "do this step" you give a goal, and the agent loops: try, check, fail, try differently, until the goal is reached. Essentially a "while goal != completed" loop. For the first time you stop leading the AI by the hand and start waiting for a result instead of the next question.

## Step 4: Subagent

Your assistant gets assistants of its own. The key phrase: each one has its own separate context window, its own working memory. The main agent conducts and keeps the big picture; subagents each dig their own hole and bring back a summary. That's how we do research: two subagents dig a topic from different angles in parallel, the main one merges.

## Step 5: Team

Agents start talking TO EACH OTHER. Not through you: directly. They argue, negotiate, split the work. At our place whole computers talk like this: my machines reach consensus on their tasks by themselves (I told that story in the episode about the courier who quit). A powerful level, and a noticeably more expensive one: every conversation burns tokens, and they do love to talk.

## Step 6: Workflow

The inversion. Until now, the AI ran the process. Now CODE runs the process, and AIs become the workforce: a script hands out tasks to dozens of agents, collects results, verifies, repeats. Essentially a program whose functions are live agents. Repeatable, predictable, scalable: a conveyor belt instead of a workshop.

## The rule of the ladder

Every step up means more autonomy and a bigger token bill. Hence the rule that will save you real money: never climb higher than the task requires. An email? Chat. A recurring routine? Skill. Big research? Subagents. A thirty-agent audit of the whole project? That's the one place for a workflow. Using an agent team for "translate this paragraph" is hauling bread home in a semi-truck.

We live on all six steps at once: skills run our content factory, subagents dig research, a team of machines negotiates between themselves, and workflows run the checks. Every episode of this show, including this one, climbs the ladder on its way to you.

## A question for you

Which step are you on right now? Chat, skills, goals, or your own subagents and teams already? Drop it in the comments: I'll collect the stats, and in one of the next episodes I'll show how to climb exactly one step up without pain.

Coming up: our ladder from the inside, one live example per step. Stay tuned.

---

The full story, in two versions:
📖 For humans, the longread: you are reading it.
🤖 For machines: the [dev log](../devlog/from-chat-to-workflow.md). Just hand it to your coding agent (Claude Code, Codex, Cursor); it is written for machines.

Curious what happens next: follow us on X https://x.com/Tony_Stef_ or Telegram @Tonyssd.

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178 (busy, six kids, still answers).

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. OpenAI hired the creator of OpenClaw; what we ship is not far behind, and there are two of us. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
