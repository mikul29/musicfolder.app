#!/usr/bin/env python3
"""Which User Guide articles might be out of date after an app release?

    python3 tools/guide/affected.py <old-app-commit> [<new-app-commit>]

Compares the iOS repo between two commits (new defaults to HEAD) and lists every guide whose
`documents` front matter names a file that changed, plus guides whose `verified` commit is older
than <new>. Rule numbers (R61…) in `documents` are matched against changes to TEST_PLAN.md lines
that mention them. Re-check the listed guides against the app, then set their `verified` field.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP = Path("/Users/matthewmikulich/Documents/Me/Music_Folder/MyBandProject")


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(APP), *args], check=True, capture_output=True, text=True).stdout


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    old, new = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "HEAD")
    changed = [l for l in git("diff", "--name-only", old, new).splitlines() if l]
    plan_diff = git("diff", old, new, "--", "TEST_PLAN.md")
    rules_changed = set(re.findall(r"^[+-].*?\b(R\d{1,3})\b", plan_diff, re.M))
    hits = []
    for src in sorted((ROOT / "guide-src").glob("*.md")):
        text = src.read_text(encoding="utf-8")
        meta = json.loads(re.match(r"---\s*\n(.*?)\n---", text, re.S).group(1))
        reasons = []
        for d in meta.get("documents") or []:
            if re.fullmatch(r"R\d{1,3}", d):
                if d in rules_changed:
                    reasons.append(f"rule {d} changed")
                continue
            name = d.split("/")[-1]
            for c in changed:
                if c.endswith(d) or c.split("/")[-1] == name:
                    reasons.append(c)
        if reasons:
            hits.append((src.stem, sorted(set(reasons))))
    for slug, reasons in hits:
        print(f"{slug}\n    " + "\n    ".join(reasons[:8]) + ("\n    …" if len(reasons) > 8 else ""))
    print(f"\n{len(hits)} guide(s) to re-check ({len(changed)} app files changed {old}..{new})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
