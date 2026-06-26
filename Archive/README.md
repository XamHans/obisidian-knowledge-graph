# Archive — pre-OKF corpus

The complete knowledge corpus as it stood **before** the OKF restructure. This is **raw material to rework incrementally** into the clean new structure — not the live graph.

- **Excluded from the OKF bundle** (`okf-build` only reads the live `Concepts/ Tools/ Hubs/ Assets/`).
- Internal wikilinks here may be broken (everything moved together) — that's fine, they get fixed during rework.

## Layout

| Folder | Count | What |
|---|---|---|
| `Concepts/` | 97 | old concept notes |
| `Tools/` | 21 | old tool/technology notes |
| `Hubs/` | 32 | old hubs + Mindmaps + 2 build-process gap reports |
| `persona_*.md` | 1 | retired persona artifact |

## How to rework a note (incremental loop)

1. Pick one note from `Archive/Concepts/` or `Archive/Tools/`.
2. Decide it still earns a place (current, general, not project-specific). If not, leave it archived.
3. Rewrite to the schema in `../CONVENTIONS.md` — start from `../Templates/`. Fix stale provenance, set real `stability` + `reviewed`, verify it against current reality.
4. Place the clean note in the live `../Concepts/` or `../Tools/`; add it to its hub's Map of Content (create the hub if needed).
5. Delete the source note from `Archive/` once promoted.
6. `python3 ../scripts/okf-build.py` to confirm it lands in the bundle with 0 broken links.

Use the `kg-contribute` skill for the same loop on new external material.
