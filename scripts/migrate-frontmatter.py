#!/usr/bin/env python3
"""migrate-frontmatter — apply the lean CONVENTIONS.md schema to knowledge notes.

Operates on top-level Concepts/, Tools/, Hubs/. Idempotent.
  - drops dead fields: persona, status, last_enriched
  - unifies tool types: technology|software|framework -> tool
  - adds the freshness layer: stability (by type, with overrides), reviewed, as_of (tools)
  - keeps everything else (hub, evidence_status, evidence_backlog, linked_hubs,
    aliases, parent_hub, child_hubs, category)

`reviewed` is seeded to a single baseline month — it is a schema-adoption stamp,
NOT a per-note accuracy audit. Update it for real when a note is actually verified.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = {"Concepts": "concept", "Tools": "tool", "Hubs": "hub"}
DROP = {"persona", "status", "last_enriched"}
TOOL_TYPES = {"technology", "software", "framework", "tool"}
REVIEWED = "2026-06"  # schema-adoption baseline

STABILITY_DEFAULT = {"concept": "stable", "tool": "volatile", "hub": "stable"}
# A few real overrides — examples that prove the override path (see CONVENTIONS.md).
STABILITY_OVERRIDE = {
    "Agentic_RAG": "evolving",
    "Self_Reflective_RAG": "evolving",
    "PGVector": "evolving",
    "Neon_Postgres": "evolving",
    "Google_Cloud_Run": "evolving",
    "Docker": "stable",
}
KEY = re.compile(r"^([a-zA-Z_][\w]*):(.*)$")


def migrate(path: Path, folder_type: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---") and (end := text.find("\n---", 3)) != -1:
        fm_lines = text[3:end].strip("\n").splitlines()
        body = text[end + 4:].lstrip("\n")
    else:
        fm_lines, body = [], text

    kept, cur, typ, have = [], None, None, set()
    for line in fm_lines:
        m = KEY.match(line)
        if m:
            key = m.group(1)
            cur = key
            if key in DROP:
                cur = None
                continue
            have.add(key)
            if key == "type":
                val = m.group(2).strip()
                typ = "tool" if val in TOOL_TYPES else (val or folder_type)
                kept.append(f"type: {typ}")
            else:
                kept.append(line)
        elif cur is not None:        # continuation line of a kept key (list item)
            kept.append(line)
        # else: continuation of a dropped key -> skip

    if typ is None:
        typ = folder_type

    add = []
    if "stability" not in have:
        add.append("stability: " + STABILITY_OVERRIDE.get(path.stem, STABILITY_DEFAULT.get(typ, "stable")))
    if typ == "tool" and "as_of" not in have:
        add.append(f"as_of: {REVIEWED}")
    if "reviewed" not in have:
        add.append(f"reviewed: {REVIEWED}")

    type_line = next((l for l in kept if l.startswith("type:")), f"type: {typ}")
    rest = [l for l in kept if not l.startswith("type:")]
    new = "---\n" + "\n".join([type_line] + add + rest) + "\n---\n\n" + body
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for d, ftype in DIRS.items():
        for p in sorted((ROOT / d).glob("*.md")):
            if migrate(p, ftype):
                changed += 1
    print(f"migrated {changed} notes (Concepts/Tools/Hubs top-level)")


if __name__ == "__main__":
    main()
