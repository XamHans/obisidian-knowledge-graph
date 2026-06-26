#!/usr/bin/env python3
"""okf-validate — fail-fast validation of the generated okf/ bundle.

Checks OKF compliance and the public/private privacy contract. Exit 0 = ok, 1 = fail.
Run after okf-build (CI runs both). This is the automated gate behind every PR.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "okf"
LINK = re.compile(r"\]\((/[^)]+\.md)\)")
PRIVATE = ("Applied", "Sources", "Daily_Notes", "Technical_Knowledge_Graph", "Archive")


def main():
    if not OUT.exists():
        print("✗ okf/ not found — run: python3 scripts/okf-build.py")
        sys.exit(1)

    files = sorted(OUT.rglob("*.md"))
    ids = {"/" + str(f.relative_to(OUT)).replace("\\", "/") for f in files}
    errors = []

    # The private layer must never appear in the bundle.
    for p in PRIVATE:
        if (OUT / p).exists():
            errors.append(f"private dir leaked into bundle: okf/{p}/")

    miss_type = broken = priv_links = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm = text.split("---", 2)[1] if text.count("---") >= 2 else ""
        if not re.search(r"(?m)^type:\s*\S", fm):       # OKF requires `type`
            miss_type += 1
            errors.append(f"missing `type`: {f.relative_to(OUT)}")
        for m in LINK.finditer(text):
            tgt = m.group(1)
            if any(tgt.startswith(f"/{p}/") for p in PRIVATE):   # no link into private layer
                priv_links += 1
                errors.append(f"link into private layer ({f.relative_to(OUT)}): {tgt}")
            elif tgt not in ids:                                  # no broken internal link
                broken += 1
                errors.append(f"broken link ({f.relative_to(OUT)}): {tgt}")

    print(f"files={len(files)} missing_type={miss_type} broken_links={broken} private_links={priv_links}")
    if errors:
        print("\nVALIDATION FAILED:")
        for e in errors[:50]:
            print("  ✗", e)
        sys.exit(1)
    print("✓ OKF bundle valid — type present, 0 broken links, privacy clean")


if __name__ == "__main__":
    main()
