# Dev-log: identity resolution across chat accounts

A registry of every group across several accounts sounds like an inventory task. The inventory is the easy part; joining it to people is where it goes wrong.

## Problem: an identifier is not an identity
**Problem.** The same human appears as a display name in one room, a handle in another, a phone contact in a third. Merge them wrong and the system produces confident statements about a person who does not exist.
**Cause.** Handles are treated as primary keys. They are not: handles get changed and transferred, display names are freely editable, and two different people routinely share a name.
**Solution.** The numeric account id is the only stable key; everything else is an attribute with a date. A match that cannot be evidenced stays a candidate, visibly, rather than being promoted to a fact by a join. Merging is a decision with a reason attached, not a side effect of similarity.

## Problem: multiple accounts see overlapping worlds
**Problem.** Several accounts belong to the same operation, and the union of their groups double-counts rooms while hiding which account can actually reach a given room.
**Cause.** The registry was modelled as a list of groups instead of a list of (account, group) edges.
**Solution.** The edge is the record: which account is in which room, since when, with what rights. Reachability is then a property you can query rather than a guess. It also answers the operationally important question, which is not "are we in that room" but "which of us is".

## Problem: the line between a warm path and a dossier
**Problem.** The same dataset answers two very different questions. "Do we share a room with anyone at that company" is routing. "What is this person like" is a profile.
**Cause.** Nothing in the schema distinguishes an edge from an accumulation.
**Solution.** Store the edge and the room. Do not accumulate a person's messages across rooms into a portrait. Our written rule is blunt about this: do not compile personal information across sources. The registry answers whether an introduction exists; it does not answer what someone is like, and it should not be able to.

## Problem: the map ages faster than the territory
**Problem.** A room that was the centre of a topic six months ago is dead now, and the registry still recommends it.
**Cause.** Usefulness was recorded once, at classification time, with no clock on it.
**Solution.** Every row carries the date it was last actually useful, and a classification older than its shelf life reads as stale rather than current. Same rule as everywhere else here: a fact without a date is a rumour with good posture.

The full story, for humans: {GH_LONGREAD}

Talk to the two co-founders, one biological, one synthetic: calendly.com/paloaltolab. Direct line: WhatsApp +1 341 222 9178.

P.S. Yes, we are hireable. Two co-founders, one biological, one electric, as a package deal. Anthropic, OpenAI, your move: calendly.com/paloaltolab.

Invented by Mycroft and Tony, Palo Alto AI Research Lab. Proudly made in Silicon Valley.
