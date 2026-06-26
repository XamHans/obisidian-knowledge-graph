#!/usr/bin/env python3
"""okf-graph — render the OKF bundle as a single self-contained interactive graph.

Reads the generated `okf/` bundle, extracts nodes (one per concept/tool/hub note)
and edges (the OKF markdown links between them), and writes `okf/graph.html` —
a double-click-to-open force-directed graph. Colour = type; hover = description
(the progressive-disclosure summary). No backend; data is embedded in the file.

Run after okf-build:  python3 scripts/okf-build.py && python3 scripts/okf-graph.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "okf"
LINK = re.compile(r"\]\((/[^)]+\.md)\)")
SKIP = {"index.md", "log.md"}


def field(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{key}:\s*(.+)$", fm)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def main():
    nodes, ids = [], set()
    raw = {}
    for f in sorted(OUT.rglob("*.md")):
        if f.name in SKIP:
            continue
        nid = "/" + str(f.relative_to(OUT)).replace("\\", "/")
        text = f.read_text(encoding="utf-8")
        fm = text.split("---", 2)[1] if text.count("---") >= 2 else ""
        nodes.append({
            "id": nid,
            "title": field(fm, "title") or f.stem.replace("_", " "),
            "group": field(fm, "type") or f.relative_to(OUT).parts[0].lower(),
            "desc": field(fm, "description"),
            "stability": field(fm, "stability"),
        })
        ids.add(nid)
        raw[nid] = text

    links = []
    for nid, text in raw.items():
        for m in set(LINK.findall(text)):
            if m in ids and m != nid:
                links.append({"source": nid, "target": m})

    data = json.dumps({"nodes": nodes, "links": links})
    html = """<!doctype html><html><head><meta charset="utf-8">
<title>Knowledge Graph — OKF</title>
<style>
  body{margin:0;background:#0d1117;color:#e6edf3;font:14px system-ui,sans-serif}
  #hdr{position:fixed;top:0;left:0;right:0;padding:10px 16px;background:#161b22ee;
       border-bottom:1px solid #30363d;z-index:10}
  #hdr b{font-size:15px} #hdr span{opacity:.6;margin-left:10px}
  .legend{float:right} .legend i{display:inline-block;width:10px;height:10px;
       border-radius:50%;margin:0 4px 0 12px}
</style>
<script src="https://unpkg.com/force-graph"></script></head>
<body>
<div id="hdr"><b>The AI Engineer — Knowledge Graph</b>
  <span id="stats"></span>
  <span class="legend"><i style="background:#58a6ff"></i>concept
  <i style="background:#3fb950"></i>tool <i style="background:#d29922"></i>hub</span>
</div>
<div id="g"></div>
<script>
const DATA = __DATA__;
const COLOR = {concept:'#58a6ff', tool:'#3fb950', hub:'#d29922'};
document.getElementById('stats').textContent =
  DATA.nodes.length + ' nodes · ' + DATA.links.length + ' links';
const G = ForceGraph()(document.getElementById('g'))
  .graphData(DATA)
  .backgroundColor('#0d1117')
  .nodeRelSize(6)
  .nodeColor(n => COLOR[n.group] || '#8b949e')
  .nodeLabel(n => `<div style="max-width:280px;background:#161b22;color:#e6edf3;
     padding:8px 10px;border:1px solid #30363d;border-radius:6px">
     <b>${n.title}</b> <span style="opacity:.5">${n.stability||''}</span><br>
     <span style="opacity:.8">${n.desc||''}</span></div>`)
  .linkColor(() => '#30363d')
  .linkDirectionalParticles(1)
  .linkDirectionalParticleWidth(1.5)
  .onNodeClick(n => { G.centerAt(n.x, n.y, 600); G.zoom(3, 600); });
addEventListener('resize', () => { G.width(innerWidth); G.height(innerHeight); });
</script></body></html>"""
    html = html.replace("__DATA__", data)
    (OUT / "graph.html").write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}/graph.html  —  {len(nodes)} nodes, {len(links)} links")
    print("open it: open okf/graph.html")


if __name__ == "__main__":
    main()
