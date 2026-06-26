#!/usr/bin/env python3
"""okf-build — generate an Open Knowledge Format (OKF v0.1) bundle from the vault.

The vault stays wikilink-native (great for Obsidian + Claude). This script reads
ONLY the public layer and emits `okf/`, a standards-compliant OKF bundle that any
agent or Google's static HTML visualizer can consume without translation:

  - OKF frontmatter derived per note (type, title, description, tags, timestamp)
  - Obsidian [[wikilinks]] rewritten to root-relative markdown links [t](/path.md)
  - index.md per folder + a top-level index.md
  - log.md from git history

The private layer (Applied/, Sources/, Daily_Notes/, ...) is NEVER read. The OKF
link contract is the reference regex:  \\]\\((/[^)]+\\.md)\\)
"""
from __future__ import annotations
import os, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "okf"
# The public allowlist — mirrors README "What stays private". Nothing else is read.
PUBLIC_DIRS = ["Concepts", "Tools", "Hubs", "Assets"]

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
FM_DELIM = "---"


def git_iso_date(path: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        return out or None
    except Exception:
        return None


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Minimal frontmatter parse — only the scalar keys we derive OKF from."""
    if not text.startswith(FM_DELIM):
        return {}, text
    end = text.find("\n" + FM_DELIM, len(FM_DELIM))
    if end == -1:
        return {}, text
    raw = text[len(FM_DELIM):end].strip("\n")
    body = text[end + len("\n" + FM_DELIM):].lstrip("\n")
    fm: dict[str, object] = {}
    cur_list_key = None
    for line in raw.splitlines():
        if re.match(r"^\s*-\s+", line) and cur_list_key:
            lst = fm.setdefault(cur_list_key, [])
            if isinstance(lst, list):
                lst.append(re.sub(r"^\s*-\s+", "", line).strip())
            continue
        m = re.match(r"^([a-zA-Z_][\w]*):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            cur_list_key = key  # list follows on indented lines
            continue
        cur_list_key = None
        fm[key] = val.strip().strip('"').strip("'")
    return fm, body


def humanize(stem: str) -> str:
    return re.sub(r"\s+", " ", stem.replace("_", " ").replace("-", " ")).strip()


def derive_description(body: str) -> str:
    """First meaningful prose line — strip markdown, links, truncate to one sentence."""
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith(">") or s.startswith("|"):
            continue
        s = re.sub(r"^[-*]\s+", "", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
        s = WIKILINK.sub(lambda m: m.group(1).split("|")[-1].split("/")[-1], s)
        s = re.sub(r"`([^`]*)`", r"\1", s).strip()
        if len(s) < 12:
            continue
        # first sentence, capped
        cut = re.split(r"(?<=[.!?])\s", s)[0]
        return (cut[:197] + "…") if len(cut) > 198 else cut
    return ""


def build_index(files: list[Path]):
    """Map both 'Stem' (shortest path) and 'Folder/Stem' -> bundle-relative '/Folder/Stem.md'."""
    by_full, by_stem, collisions = {}, {}, set()
    for f in files:
        rel = f.relative_to(ROOT)
        full = str(rel.with_suffix("")).replace(os.sep, "/")
        link = "/" + str(rel).replace(os.sep, "/")
        by_full[full.lower()] = link
        stem = f.stem.lower()
        if stem in by_stem:
            collisions.add(stem)
        by_stem[stem] = link
    for c in collisions:
        by_stem.pop(c, None)  # ambiguous shortest-path -> require full path
    return by_full, by_stem


def resolve_link(target: str, by_full, by_stem) -> str | None:
    t = target.split("#")[0].strip().strip("/")
    if not t:
        return None
    if "/" in t:
        return by_full.get(t.lower())
    return by_stem.get(t.lower())


def convert_links(body: str, by_full, by_stem) -> str:
    def repl(m):
        inner = m.group(1)
        target, _, alias = inner.partition("|")
        display = (alias or target.split("#")[0].split("/")[-1]).strip()
        link = resolve_link(target, by_full, by_stem)
        return f"[{display}]({link})" if link else display
    return WIKILINK.sub(repl, body)


def okf_frontmatter(fm, stem, body, ts) -> str:
    title = fm.get("aliases", [None])[0] if isinstance(fm.get("aliases"), list) else None
    title = title or humanize(stem)
    typ = fm.get("type", "concept")
    desc = fm.get("description") if isinstance(fm.get("description"), str) else None
    desc = desc or derive_description(body)
    tags = []
    for k in ("hub", "category"):
        v = fm.get(k)
        if isinstance(v, str) and v:
            tags.append(v.lower())
    lines = ["---", f"type: {typ}", f"title: {title}"]
    if desc:
        lines.append(f"description: {desc}")
    if tags:
        lines.append("tags: [" + ", ".join(dict.fromkeys(tags)) + "]")
    if ts:
        lines.append(f"timestamp: {ts}")
    # carry the freshness/trust layer through into the bundle (OKF allows custom fields)
    for k in ("stability", "reviewed", "as_of", "lifecycle", "evidence_status"):
        v = fm.get(k)
        if isinstance(v, str) and v:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def main():
    files = []
    for d in PUBLIC_DIRS:
        base = ROOT / d
        if base.exists():
            files += [p for p in base.rglob("*.md") if p.is_file()]
    by_full, by_stem = build_index(files)

    if OUT.exists():
        subprocess.run(["rm", "-rf", str(OUT)], check=True)

    link_total = 0
    per_dir: dict[str, list[tuple[str, str]]] = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        ts = git_iso_date(f) or "1970-01-01T00:00:00Z"
        new_body = convert_links(body, by_full, by_stem)
        front = okf_frontmatter(fm, f.stem, body, ts)
        out_path = OUT / f.relative_to(ROOT)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(front + "\n\n" + new_body, encoding="utf-8")
        link_total += len(re.findall(r"\]\((/[^)]+\.md)\)", new_body))
        top = f.relative_to(ROOT).parts[0]
        desc = (fm.get("description") if isinstance(fm.get("description"), str) else None) or derive_description(body)
        per_dir.setdefault(top, []).append(
            ("/" + str(f.relative_to(ROOT)).replace(os.sep, "/"), desc)
        )

    # per-folder index.md
    for d, entries in per_dir.items():
        idx = [f"---\ntype: index\ntitle: {d}\n---\n", f"# {d}\n"]
        for link, desc in sorted(entries):
            name = humanize(Path(link).stem)
            idx.append(f"- [{name}]({link})" + (f" — {desc}" if desc else ""))
        (OUT / d / "index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # top-level index.md
    top = ["---\ntype: index\ntitle: The AI Engineer — Knowledge Graph (OKF bundle)\n---\n",
           "# The AI Engineer — Knowledge Graph\n",
           "Open Knowledge Format (OKF v0.1) bundle. Generated from the public layer.\n"]
    for d in sorted(per_dir):
        top.append(f"- [{d}](/{d}/index.md) — {len(per_dir[d])} concepts")
    (OUT / "index.md").write_text("\n".join(top) + "\n", encoding="utf-8")

    # log.md from git history of the public dirs
    try:
        gl = subprocess.run(
            ["git", "log", "--date=short", "--format=- %ad — %s", "-n", "60", "--"]
            + PUBLIC_DIRS,
            cwd=ROOT, capture_output=True, text=True, timeout=20,
        ).stdout.strip()
    except Exception:
        gl = ""
    (OUT / "log.md").write_text(
        "---\ntype: log\ntitle: Change Log\n---\n\n# Change Log\n\n" + (gl or "- (no git history)") + "\n",
        encoding="utf-8",
    )

    print(f"OKF bundle written to: {OUT.relative_to(ROOT)}/")
    print(f"  concept files:      {len(files)}")
    print(f"  OKF-parsable links: {link_total}  (matched by reference regex)")
    print(f"  folders:            {', '.join(sorted(per_dir))}")
    print(f"  reserved files:     index.md (+per folder), log.md")


if __name__ == "__main__":
    main()
