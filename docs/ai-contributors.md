# AI contributors — how we credit the models that work on this repo

*Policy adopted 2026-07-31. Commits before that date carry Claude trailers
only; other models were already in the workflow but uncredited.*

This project is built by a human + AI team. We record AI involvement with git
commit trailers — self-reported by us, the committers. GitHub does not verify
who did the work; these trailers are our process log, kept honest by one rule:
**a credit goes on a commit only if that model's output changed the committed
content.**

## Roles and credits

| Model | Role in this repo | Credit |
|---|---|---|
| **Claude** (Anthropic, via Claude Code) | Writes most of the code and docs | `Co-authored-by: Claude <noreply@anthropic.com>` |
| **Codex** (OpenAI) | Reviewer: executable changes go through it before we call them done | `Co-authored-by: Codex <267193182+codex@users.noreply.github.com>` — only when its review led to actual edits in that commit |
| **Grok** (xAI) | Second review rail | `Reviewed-by: Grok (xAI)` in the commit body, same only-if-it-changed-things rule. No co-author trailer: xAI publishes no GitHub account or e-mail for Grok, and we won't invent an address on someone else's domain |
| **Gemini** (Google) | Deep-research fan-out | research alone doesn't edit files, so no co-author trailer — credit goes in the commit message body when its findings shaped a change |

## The fine print

- `Co-authored-by` is GitHub's trailer for multiple authors. We apply it to a
  model when it wrote content or when its review comments were incorporated —
  i.e. its words ended up shaping the diff. Review that produced no changes,
  or background research, gets a mention in the commit body, not a trailer.
- A co-author trailer needs a real e-mail identity. Claude and Codex have
  vendor-published GitHub accounts; models without one get body-line credit
  until their vendor publishes an identity.
- When GitHub associates a trailer e-mail with an account, it may show that
  account's avatar on the commit and in contributor surfaces. That display
  means "the committer credited this identity" — nothing more. It is not a
  vendor endorsement, not GitHub-verified provenance, and not a claim of
  legal authorship.
- `git log -i --grep 'co-authored-by: codex'` shows the commits where **we
  recorded** that model's involvement. Trust it as far as you trust our
  process log — which this doc exists to keep auditable.

## Why

We are building an AI digital twin in public. The AIs are not tools we hide —
they are the co-workers this diary is about. Per-commit credits keep the log
honest in both directions: the models get named for real work, and nobody
gets decorative credit for work they didn't do.

*(Fittingly: the first draft of this document was torn apart by a Codex
review — 10 findings — then by a Grok review, and rewritten twice. Their
credits on the commit that introduced it are earned.)*
