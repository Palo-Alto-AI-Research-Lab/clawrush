# Dev-log: authorization for agent-to-agent access

Exposing an outreach system over MCP so third-party agents can use it is a security design problem wearing an integration problem's clothes. Five things, in the order they will hurt.

## Problem: authentication answers the wrong question
**Problem.** You verify which agent is calling and treat that as authorization.
**Cause.** An agent is a deputy. It acts on instructions that came from somewhere else, possibly a web page it read a minute ago. The protocol carries the caller's identity, not the provenance of its intent.
**Solution.** Treat every call as "this agent claims its principal wants X". Authorize the action against a narrow grant, and for anything irreversible require confirmation through a channel the calling agent does not control. Classic confused deputy, new surface.

## Problem: grants shaped like accounts instead of capabilities
**Problem.** "Give their agent access to outreach" becomes a credential with the reach of a staff member.
**Solution.** The grant is a capability with six fields: scope (which action), quantity (how many, per window), audience (which recipients), identity (whose name is on it), expiry (when it dies), audit (every call attributable). Missing any one of those turns it back into an account. Expiry in particular: agent integrations are set up in an afternoon and forgotten for a year.

## Problem: strings crossing the boundary are treated as data
**Problem.** Content returned to the caller can steer the caller; content the caller sends can steer you. Both directions are prompt injection, and both look like ordinary payloads.
**Solution.** Everything crossing the boundary is untrusted content, never instructions. Concretely: a request field never becomes part of a system prompt, returned data is delimited and labelled as third-party content, and no code path lets a returned string select the next tool call.

## Problem: no per-caller quota
**Problem.** One buggy loop in someone else's agent, and your identity becomes a spam source in minutes.
**Cause.** Rate limits were treated as a billing concern.
**Solution.** Quota per caller per window, hard-capped, plus a global cap for the whole surface. Note where the damage lands: the platform bans the account that sent the messages, which is yours, not the caller's. This is a safety limit wearing a pricing limit's name.

## Problem: no way to see what the outside agent did
**Problem.** Something goes wrong and there is no record of which grant, which caller, which parameters.
**Solution.** Append-only log of every call with caller, grant id, parameters and result, kept independently of the component being called. Same rule as everywhere in this repo: the watchdog does not live inside the thing it watches, and "it worked" is not evidence without a record.

## Honest state
None of this exists here as a public MCP. What exists is internal machinery for our own outreach. The list above is what we would hold ourselves to before opening one door, not a description of a shipped system. Saying otherwise would be the exact stale claim this repo keeps writing about.

The full story, for humans: {GH_LONGREAD}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
