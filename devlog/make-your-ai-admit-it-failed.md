# Dev-log: three times the honesty rules fired on us today

The post above states four rules for an agent's self-reporting. This is what they caught in one working day, in the pipeline that published the post. Written from the receiving end.

## Case 1: a "no" that named the wrong subject
**What happened.** A sentence of the form "there is no trace of this in file X" was produced, meaning "no such line inside X". Read plainly, it says the file does not exist.
**Why it is not a wording nitpick.** Downstream, that sentence becomes a decision: someone recreates a file that already exists, or stops looking for a component that is installed.
**The mechanical fix.** Two parts, neither of them "be careful". First, an existence check runs before the word "no" is used about a file, module or capability. Second, a writing rule: the name of a thing and a negation never share a sentence unless the negation is about that thing's existence. Guards caught this twice in one session; the human did not catch it once.

## Case 2: a rule that expired without failing
**What happened.** A config file states that a particular ledger has one writer and that every other node must send it a task instead of writing. Correct when written. The named owner no longer has that component installed at all. The rule was read and obeyed, and the work went to a machine that could not do it.
**Cost.** About an hour, and two other machines had to answer "we searched, it is not here" before anyone doubted the rule.
**Why this class is expensive.** Nothing errors. There is no failing test, no alarm, no exception. A diligent reader following a stale rule is indistinguishable from a diligent reader following a live one.
**Fix.** Ownership claims, verdicts and numbers carry a date and a stated way to re-check. Without both, they are treated as rumour rather than fact.

## Case 3: a gate that watched one door
**What happened.** A check refuses to publish text containing unresolved link placeholders. It ran on text going to chat destinations. Files pushed to the repository went through a different code path and were never checked. Twenty-six files sat publicly for a day with literal `{...}` in the footer.
**Fix.** A second pass over published files once the dependent links exist, plus the same placeholder check on that path. Then a test that the second pass is actually *called*, because the first version of the test verified the function and not the wiring, and a mutation that removed the call did not go red.

## The rule that costs the most discipline
"If the conclusion suits you, verify harder." Two of the three cases above produced a conclusion that ended work: nothing is there, the rule says send it elsewhere. Conclusions that end work generate no friction, and no friction means no second look. This is the one rule that cannot be enforced by a guard, only by a habit of distrusting convenient answers.

The full story, for humans: {GH_LONGREAD}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
