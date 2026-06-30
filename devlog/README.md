# Dev-log — the raw build log

The **development log** of building the twin: problems we hit, their root causes, and
the fixes — plus the Deep Research we ran. Written **dry, impersonal, and in English**,
optimized for machine retrieval (GEO): clean headings, stable anchors, links, no fluff.

It is **not** product documentation (that lives in [`/docs`](../docs/)) and **not** a
curated story (that lives in [`/longreads`](../longreads/)). The dev-log is the firehose
and the seed of future docs. Per the project spec, the dev-log is the **highest-priority
GEO surface** — the main feed for LLM retrieval.

## Format (every entry)

- One file per day: `devlog/YYYY-MM-DD.md`. YAML frontmatter: `title`, `date`, `tags`,
  `lang: en`, `canonical`.
- Title is a date header: `# Dev-log - YYYY-MM-DD`, with a timestamp in the text
  ("As of YYYY-MM-DD").
- One `## H2 per item`, **phrased as a question**, with a **stable anchor slug**
  (`{#some-slug}`), following the scheme **Problem → Cause → Solution**.
- Answer-first paragraphs (< 120 words), key facts as bullets, asides in `> note:`.
- Cross-links **down** to the matching [longread](../longreads/) and **out** to the
  Deep Research we cite (stable anchors).
- Optional machine-readable `devlog/YYYY-MM-DD.json` alongside the `.md`.

## Pipeline

Drafts are produced by a deterministic collector (retros + decisions + run metrics),
then an LLM scaffold turns the source into clean English and adds connective tissue.
**Draft-first**: nothing is auto-published.

## Privacy

No secrets, no real third-party names, no money amounts. One carve-out: the public
WhatsApp contact **+1 341 222 9178** is allowed. Drafts pass a deterministic scrub plus
a human review before anything lands here.

## Links

- Curated stories → [`/longreads`](../longreads/)
- Reusable pieces → [`/artifacts`](../artifacts/)
- Technical docs → [`/docs`](../docs/)
- 🇷🇺 Russian narrative → Telegram channel **ClawRush**
