# -*- coding: utf-8 -*-
"""Tests for tools/build_feed.py.  Run:  python tools/_test_build_feed.py

No test framework, no network, no git writes. Exit 0 = green, 1 = red.
"""
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_feed as bf  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("  ok   " if cond else "  FAIL ") + name + ((" — " + detail) if detail and not cond else ""))
    if not cond:
        fails.append(name)


print("parse_post")
title, summary = bf.parse_post("# Hello world\n\nFirst **para** with a [link](http://x).\n\nSecond.")
check("title from first heading", title == "Hello world", repr(title))
check("summary is markdown-stripped", summary == "First para with a link.", repr(summary))

title, _ = bf.parse_post("no heading at all\n\ntext")
check("no heading -> None", title is None, repr(title))

_, summary = bf.parse_post("# T\n\n> a quote\n\n| a | table |\n\nReal paragraph.")
check("skips quote/table blocks", summary == "Real paragraph.", repr(summary))

_, summary = bf.parse_post("# T\n\n" + "word " * 200)
check("summary truncated", len(summary) <= bf.SUMMARY_CHARS + 1 and summary.endswith("…"), repr(summary[-20:]))

print("rfc822")
check("iso -> rfc822 utc", bf.rfc822("2026-07-31T21:57:26-07:00") == "Sat, 01 Aug 2026 04:57:26 +0000",
      bf.rfc822("2026-07-31T21:57:26-07:00"))

print("ordering and links (regressions found by an external review, 2026-08-01)")
mixed = [{"title": "later", "summary": "", "link": "http://x/a", "iso": "2026-07-31T23:00:00-10:00"},
         {"title": "earlier", "summary": "", "link": "http://x/b", "iso": "2026-08-01T01:00:00+14:00"}]
ordered = sorted(mixed, key=lambda p: bf.datetime.fromisoformat(p["iso"]).astimezone(bf.timezone.utc),
                 reverse=True)
check("mixed timezone offsets sort by instant, not by string",
      ordered[0]["title"] == "later", ordered[0]["title"])

check("spaces and # in a filename are percent-encoded",
      "a%20b%23c.md" in bf.urllib.parse.quote("longreads/a b#c.md"),
      bf.urllib.parse.quote("longreads/a b#c.md"))
check("path separators survive quoting",
      bf.urllib.parse.quote("longreads/x.md") == "longreads/x.md")

print("render")
xml = bf.render([{"title": "A & B <tag>", "summary": "s & s", "link": "http://x/a.md",
                  "iso": "2026-07-31T10:00:00+00:00"}], "Fri, 01 Aug 2026 00:00:00 +0000")
try:
    root = ET.fromstring(xml)
    ok = True
except ET.ParseError as exc:
    root, ok = None, False
    print("     ", exc)
check("output is well-formed XML even with & and <>", ok)
if ok:
    item = root.find("./channel/item")
    check("title survives escaping", item.findtext("title") == "A & B <tag>", item.findtext("title"))
    check("guid == link", item.findtext("guid") == item.findtext("link"))

print("live repo")
posts = bf.collect()
check("finds essays in longreads/", len(posts) > 0, "%d found" % len(posts))
check("every post has a date", all(p["iso"] for p in posts))
inst = [bf.datetime.fromisoformat(p["iso"]).astimezone(bf.timezone.utc) for p in posts]
check("sorted newest first (by instant — this repo really does hold mixed offsets)",
      all(inst[i] >= inst[i + 1] for i in range(len(inst) - 1)))
try:
    ET.fromstring(bf.render(posts, "Fri, 01 Aug 2026 00:00:00 +0000"))
    check("real feed parses", True)
except ET.ParseError as exc:
    check("real feed parses", False, str(exc))

print()
if fails:
    print("RED — %d failed: %s" % (len(fails), ", ".join(fails)))
    sys.exit(1)
print("GREEN — all checks passed")
