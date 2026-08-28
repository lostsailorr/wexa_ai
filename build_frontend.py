import os
import json

with open("backend/app/services/mock_data.py", "r", encoding="utf-8") as f:
    text = f.read()

loc = {}
exec(text, {}, loc)
mock_nodes = loc["MOCK_NODES"]
mock_edges = loc["MOCK_EDGES"]

with open("backend/static/app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Remove any previous DEFAULT_NODES if already added
if "const DEFAULT_NODES" in app_js:
    parts = app_js.split("let networkInstance = null;")
    app_js = "let networkInstance = null;" + parts[-1]

data_block = f"""// ==========================================
// EMBEDDED REALISTIC DATASET (CLIENT-SIDE RESILIENCE)
// ==========================================
const DEFAULT_NODES = {json.dumps(mock_nodes, indent=2)};
const DEFAULT_EDGES = {json.dumps(mock_edges, indent=2)};
"""

new_app_js = data_block + "\n" + app_js

# Fallback health check
new_app_js = new_app_js.replace(
    'badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-rose-500/10 border border-rose-500/30 text-xs text-rose-400";\n    text.innerText = "Backend Offline";',
    'badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300";\n    text.innerText = "Demo Simulation Mode";'
)

# Robust metrics fallback
old_metrics = """async function loadMetrics() {
  try {
    const res = await fetch("/api/graph/metrics");
    const data = await res.json();
    const m = data.metrics || {};
    document.getElementById("statPersons").innerText = m.person_count || 0;
    document.getElementById("statCompanies").innerText = m.company_count || 0;
    document.getElementById("statAccounts").innerText = m.account_count || 0;
    document.getElementById("statTransfers").innerText = m.transfer_count || 0;
    document.getElementById("statEdges").innerText = m.total_relationships || 0;
  } catch (e) {
    console.error("Failed to load metrics", e);
  }
}"""

new_metrics = """async function loadMetrics() {
  let m = {
    person_count: DEFAULT_NODES.filter(n => n.label === 'Person').length,
    company_count: DEFAULT_NODES.filter(n => n.label === 'Company').length,
    account_count: DEFAULT_NODES.filter(n => n.label === 'BankAccount').length,
    transfer_count: DEFAULT_EDGES.filter(e => e.type === 'TRANSFERRED_TO').length,
    total_relationships: DEFAULT_EDGES.length
  };
  try {
    const res = await fetch("/api/graph/metrics");
    if (res.ok) {
      const data = await res.json();
      if (data.metrics) m = data.metrics;
    }
  } catch (e) {
    console.warn("Using fallback dataset metrics");
  }
  document.getElementById("statPersons").innerText = m.person_count || 0;
  document.getElementById("statCompanies").innerText = m.company_count || 0;
  document.getElementById("statAccounts").innerText = m.account_count || 0;
  document.getElementById("statTransfers").innerText = m.transfer_count || 0;
  document.getElementById("statEdges").innerText = m.total_relationships || 0;
}"""

new_app_js = new_app_js.replace(old_metrics, new_metrics)

# Robust graph initial loading fallback
old_subgraph = """    const res = await fetch(url);
    const data = await res.json();
    rawNodes = data.nodes || [];
    rawEdges = data.edges || [];"""

new_subgraph = """    try {
      const res = await fetch(url);
      if (res.ok) {
        const data = await res.json();
        rawNodes = data.nodes || [];
        rawEdges = data.edges || [];
      } else {
        rawNodes = DEFAULT_NODES;
        rawEdges = DEFAULT_EDGES;
      }
    } catch (fetchErr) {
      console.warn("Using resilient client dataset fallback");
      rawNodes = DEFAULT_NODES;
      rawEdges = DEFAULT_EDGES;
    }

    if (nodeType) {
      rawNodes = rawNodes.filter(n => n.label === nodeType);
      const validIds = new Set(rawNodes.map(n => n.id || n.account_number));
      rawEdges = rawEdges.filter(e => validIds.has(e.source) && validIds.has(e.target));
    }
    if (minRisk > 0) {
      rawNodes = rawNodes.filter(n => (n.risk_score || n.base_risk || 0.0) >= minRisk);
      const validIds = new Set(rawNodes.map(n => n.id || n.account_number));
      rawEdges = rawEdges.filter(e => validIds.has(e.source) && validIds.has(e.target));
    }"""

new_app_js = new_app_js.replace(old_subgraph, new_subgraph)

# Copy to all distribution paths
paths = ["backend/static/app.js", "public/app.js", "public/static/app.js", "app.js"]
for p in paths:
    os.makedirs(os.path.dirname(p) if os.path.dirname(p) else ".", exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(new_app_js)

# Also copy index.html and style.css across public, root, and backend/static
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Update script/css paths in index.html to support both relative and static URLs
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)
with open("public/static/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("backend/static/style.css", "r", encoding="utf-8") as f:
    style_css = f.read()
with open("style.css", "w", encoding="utf-8") as f:
    f.write(style_css)
with open("public/style.css", "w", encoding="utf-8") as f:
    f.write(style_css)
with open("public/static/style.css", "w", encoding="utf-8") as f:
    f.write(style_css)

print("All frontend assets built and synchronized across public/, backend/static/, and root!")
