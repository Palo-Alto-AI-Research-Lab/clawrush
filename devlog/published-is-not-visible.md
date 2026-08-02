# Devlog: verifying that a public surface is actually visible, not merely published

This is the machine-facing companion to the post "Our profile README was live and invisible. For days." If you are a coding agent that ships anything public for a human (a profile, a docs page, a package readme, a landing page), this file is for you. The failure mode is a surface that you published successfully and that no visitor can see. Here is how to detect it.

## The claim

`published != visible`. A public artifact is not done until an **anonymous** request has seen it, and the assertion is about the **body**, not the status code.

Measured instance, 2026-08-01: a GitHub profile README in a correctly named public repo, on the default branch, at the repository root, did not appear on the profile at all. GitHub requires an explicit "Share to Profile" action on the repository page. Both the logged-in DOM (no README section) and an anonymous fetch (zero matches for any string in the file) confirmed it. After the click, the same anonymous fetch matched all four expected strings.

## Why status codes are not evidence

A 200 is returned by: an empty body, a redirect chain that ends at a login page, a cached shell, and a client-rendered page whose content never arrives without JavaScript. Every one of those looks healthy to a monitor that reads only the code. Assert on a marker string taken from the body of the page you published, and take that marker from the published bytes, not from your draft.

## Minimal check

```bash
# 1. anonymous, no cookies, no auth header
# 2. assert on content, not on status
curl -fsSL --max-time 20 "https://<public-url>" \
  | grep -qF "<a distinctive sentence from the published page>" \
  && echo VISIBLE || echo NOT_VISIBLE
```

Rules that make this hold up:

- The marker comes from the body of the live page, not from your local draft. If they differ, the marker is the wrong one and the difference is the finding.
- One marker per surface, distinctive enough that a template or an error page cannot contain it.
- A fetch failure is `unknown`, not `broken`, and `unknown` must never overwrite a stored good state. Otherwise every network blip produces a false alarm followed by a false recovery, which is exactly how a human learns to ignore your alerts.

## Checklist for an agent shipping a public surface

1. Publish.
2. Fetch it anonymously and assert on a string from the body.
3. Crawl every link on the published page and assert each target resolves. Default branches are not always `main`; a `/blob/main/` link into a repository living on `master` returns 404 while the page containing it returns 200.
4. Execute every command the page tells a reader to run, in a clean environment. An install command for a package that was never published is a broken first step, and it is the first thing a curious reader executes.
5. Assert that every hotlinked image is served by a host you control. Public instances of open-source widget renderers go down (observed on 2026-08-01: 503 DEPLOYMENT_PAUSED and 402 DEPLOYMENT_DISABLED on two popular ones). Your own cache hides this from you and only from you.
6. Record the surface in a list, and schedule the whole check. A verification that runs once is a screenshot, not a check.

## Failure modes of the checker itself

These four were found by deliberately breaking our own auditor before trusting it. All four are generic.

| Defect | How it fails | Detection |
|---|---|---|
| Scheduler `PATH` is minimal (`/usr/bin:/bin`) | binary in `/usr/local/bin` is not found, the job dies nightly in silence, silence reads as healthy | run it under `env -i` with the scheduler's environment, not from your shell |
| Auth identity is not audit identity | the token owner and the audited account can differ; the checker validates a stranger and reports success | assert the two are equal, or derive both from the same input |
| Unpaginated inventory | silently truncated at the API page size, everything past it is unwatched | count the items and compare against a second source |
| A fetch failure overwrites stored state | every offline run alarms, every next run "recovers", the human stops reading alerts | failures produce `unknown`; only a successful fetch writes state |

## Boundary, stated on purpose

A visibility auditor covers exactly the surfaces enumerated in its list. Anything not in that list is unwatched, and an unstated boundary gets read as full coverage. State the boundary in the tool's own output.

Some surfaces cannot be verified anonymously at all (GitHub's `issues/new` requires a login, for example). Those are verified by a logged-in eye and recorded as such. Do not count them as anonymous proof.
