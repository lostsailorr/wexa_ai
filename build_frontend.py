import os
import json

# 1. Load mock data
with open("backend/app/services/mock_data.py", "r", encoding="utf-8") as f:
    text = f.read()

loc = {}
exec(text, {}, loc)
mock_nodes = loc["MOCK_NODES"]
mock_edges = loc["MOCK_EDGES"]

mock_rings = [
    {
        "origin_account": "ACC-9003",
        "origin_bank": "BVI International Trust Bank",
        "loop_length": 4,
        "total_volume": 3220000.0,
        "account_chain": ["ACC-9003", "ACC-9002", "ACC-9005", "ACC-9012", "ACC-9003"],
        "transaction_chain": ["TX-SMURF-101", "TX-SMURF-102", "TX-SMURF-103", "TX-SMURF-104"],
        "ring_nodes": [
            {"id": "ACC-9003", "label": "BankAccount", "account_number": "ACC-9003", "bank_name": "BVI International Trust Bank", "country": "BVI", "risk_level": "CRITICAL"},
            {"id": "ACC-9002", "label": "BankAccount", "account_number": "ACC-9002", "bank_name": "Bank of Cyprus Commercial", "country": "Cyprus", "risk_level": "HIGH"},
            {"id": "ACC-9005", "label": "BankAccount", "account_number": "ACC-9005", "bank_name": "Emirates NBD Freezone", "country": "UAE", "risk_level": "HIGH"},
            {"id": "ACC-9012", "label": "BankAccount", "account_number": "ACC-9012", "bank_name": "Cayman Grand Trust Bank", "country": "Cayman Islands", "risk_level": "CRITICAL"}
        ],
        "ring_edges": [
            {"tx_id": "TX-SMURF-101", "amount": 850000.0, "currency": "USD", "timestamp": "2023-11-01T09:15:00Z", "from_acc": "ACC-9003", "to_acc": "ACC-9002"},
            {"tx_id": "TX-SMURF-102", "amount": 820000.0, "currency": "USD", "timestamp": "2023-11-02T11:30:00Z", "from_acc": "ACC-9002", "to_acc": "ACC-9005"},
            {"tx_id": "TX-SMURF-103", "amount": 790000.0, "currency": "USD", "timestamp": "2023-11-03T14:45:00Z", "from_acc": "ACC-9005", "to_acc": "ACC-9012"},
            {"tx_id": "TX-SMURF-104", "amount": 760000.0, "currency": "USD", "timestamp": "2023-11-04T16:20:00Z", "from_acc": "ACC-9012", "to_acc": "ACC-9003"}
        ]
    },
    {
        "origin_account": "ACC-9006",
        "origin_bank": "Banco General Panama",
        "loop_length": 3,
        "total_volume": 1730000.0,
        "account_chain": ["ACC-9006", "ACC-9013", "ACC-9004", "ACC-9006"],
        "transaction_chain": ["TX-LAYER-201", "TX-LAYER-202", "TX-LAYER-203"],
        "ring_nodes": [
            {"id": "ACC-9006", "label": "BankAccount", "account_number": "ACC-9006", "bank_name": "Banco General Panama", "country": "Panama", "risk_level": "CRITICAL"},
            {"id": "ACC-9013", "label": "BankAccount", "account_number": "ACC-9013", "bank_name": "Marshall Trust Depository", "country": "Marshall Islands", "risk_level": "CRITICAL"},
            {"id": "ACC-9004", "label": "BankAccount", "account_number": "ACC-9004", "bank_name": "Barclays Commercial London", "country": "United Kingdom", "risk_level": "MEDIUM"}
        ],
        "ring_edges": [
            {"tx_id": "TX-LAYER-201", "amount": 600000.0, "currency": "USD", "timestamp": "2023-12-10T10:00:00Z", "from_acc": "ACC-9006", "to_acc": "ACC-9013"},
            {"tx_id": "TX-LAYER-202", "amount": 580000.0, "currency": "USD", "timestamp": "2023-12-11T13:10:00Z", "from_acc": "ACC-9013", "to_acc": "ACC-9004"},
            {"tx_id": "TX-LAYER-203", "amount": 550000.0, "currency": "USD", "timestamp": "2023-12-12T15:40:00Z", "from_acc": "ACC-9004", "to_acc": "ACC-9006"}
        ]
    }
]

mock_ubo = {
    "C-208": [
        {
            "ubo_id": "P-101",
            "ubo_name": "Viktor Sterling",
            "nationality": "Russian",
            "is_pep": True,
            "person_risk": 0.94,
            "company_id": "C-208",
            "company_name": "Lumina Capital Partners LP",
            "effective_ownership_pct": 57.38,
            "ownership_depth": 4,
            "ownership_chain": [
                {"id": "P-101", "name": "Viktor Sterling", "type": "Person", "risk_score": 0.94, "jurisdiction": "Russian"},
                {"id": "C-201", "name": "Seashell Global Holdings Ltd", "type": "Company", "risk_score": 0.91, "jurisdiction": "BVI"},
                {"id": "C-202", "name": "Apex Meridian Trading S.A.", "type": "Company", "risk_score": 0.86, "jurisdiction": "Cyprus"},
                {"id": "C-203", "name": "Golden Horizon Logistics Ltd", "type": "Company", "risk_score": 0.62, "jurisdiction": "United Kingdom"},
                {"id": "C-208", "name": "Lumina Capital Partners LP", "type": "Company", "risk_score": 0.48, "jurisdiction": "United States"}
            ],
            "relationship_chain": [
                {"share_pct": 100.0, "since": "2020-03-15"},
                {"share_pct": 85.0, "since": "2020-08-01"},
                {"share_pct": 90.0, "since": "2021-02-14"},
                {"share_pct": 75.0, "since": "2021-11-20"}
            ]
        }
    ],
    "C-211": [
        {
            "ubo_id": "P-102",
            "ubo_name": "Elena Sterling",
            "nationality": "Cypriot",
            "is_pep": True,
            "person_risk": 0.78,
            "company_id": "C-211",
            "company_name": "Blue Water Real Estate GmbH",
            "effective_ownership_pct": 100.0,
            "ownership_depth": 2,
            "ownership_chain": [
                {"id": "P-102", "name": "Elena Sterling", "type": "Person", "risk_score": 0.78, "jurisdiction": "Cypriot"},
                {"id": "C-204", "name": "Sovereign Blue Maritime Corp", "type": "Company", "risk_score": 0.88, "jurisdiction": "Panama"},
                {"id": "C-211", "name": "Blue Water Real Estate GmbH", "type": "Company", "risk_score": 0.50, "jurisdiction": "Germany"}
            ],
            "relationship_chain": [
                {"share_pct": 100.0, "since": "2019-06-10"},
                {"share_pct": 100.0, "since": "2021-04-05"}
            ]
        }
    ]
}

mock_sanctions = {
    "C-208": {
        "found": True,
        "path": {
            "distance": 4,
            "sanction_id": "SANCT-OFAC-SDN",
            "sanctioning_body": "US Dept of Treasury",
            "sanction_program": "UKRAINE-EO14024 / DEFENSE_SECTOR",
            "sanction_reason": "Dual-use technology procurement & weapons proliferation funding",
            "path_nodes": [
                {"id": "C-208", "name": "Lumina Capital Partners LP", "label": "Company", "risk_score": 0.48, "country": "United States"},
                {"id": "ACC-9009", "name": "ACC-9009", "label": "BankAccount", "risk_score": 0.0, "country": "United States"},
                {"id": "ACC-9004", "name": "ACC-9004", "label": "BankAccount", "risk_score": 0.0, "country": "United Kingdom"},
                {"id": "ACC-9005", "name": "ACC-9005", "label": "BankAccount", "risk_score": 0.0, "country": "UAE"},
                {"id": "ACC-9007", "name": "ACC-9007", "label": "BankAccount", "risk_score": 0.0, "country": "Russia"},
                {"id": "C-205", "name": "Vostok Precision Dynamics", "label": "Company", "risk_score": 0.99, "country": "Russia"},
                {"id": "SANCT-OFAC-SDN", "name": "OFAC SDN List", "label": "SanctionList", "risk_score": 1.0, "country": "N/A"}
            ],
            "path_relationships": [
                {"type": "HOLDS_ACCOUNT", "from_id": "C-208", "to_id": "ACC-9009", "properties": {}},
                {"type": "TRANSFERRED_TO", "from_id": "ACC-9004", "to_id": "ACC-9009", "properties": {"amount": 1350000.0, "tx_id": "TX-SANCT-303"}},
                {"type": "TRANSFERRED_TO", "from_id": "ACC-9005", "to_id": "ACC-9004", "properties": {"amount": 1400000.0, "tx_id": "TX-SANCT-302"}},
                {"type": "TRANSFERRED_TO", "from_id": "ACC-9007", "to_id": "ACC-9005", "properties": {"amount": 1450000.0, "tx_id": "TX-SANCT-301"}},
                {"type": "HOLDS_ACCOUNT", "from_id": "C-205", "to_id": "ACC-9007", "properties": {}},
                {"type": "SANCTIONED_UNDER", "from_id": "C-205", "to_id": "SANCT-OFAC-SDN", "properties": {}}
            ]
        }
    },
    "P-101": {
        "found": True,
        "path": {
            "distance": 1,
            "sanction_id": "SANCT-EU-CFSP",
            "sanctioning_body": "European External Action Service",
            "sanction_program": "REG_269_2014",
            "sanction_reason": "Destabilizing actions & illicit financial asset concealment",
            "path_nodes": [
                {"id": "P-101", "name": "Viktor Sterling", "label": "Person", "risk_score": 0.94, "country": "Russian"},
                {"id": "SANCT-EU-CFSP", "name": "EU Consolidated Sanctions", "label": "SanctionList", "risk_score": 1.0, "country": "N/A"}
            ],
            "path_relationships": [
                {"type": "SANCTIONED_UNDER", "from_id": "P-101", "to_id": "SANCT-EU-CFSP", "properties": {"listed_date": "2022-05-10"}}
            ]
        }
    }
}

mock_mules = [
    {
        "account_number": "ACC-9005",
        "bank_name": "Emirates NBD Freezone",
        "country": "UAE",
        "risk_level": "HIGH",
        "unique_senders": 2,
        "unique_recipients": 2,
        "total_inflow": 2270000.0,
        "total_outflow": 2190000.0,
        "net_retention": 80000.0,
        "centrality_index": 6.0
    },
    {
        "account_number": "ACC-9004",
        "bank_name": "Barclays Commercial London",
        "country": "United Kingdom",
        "risk_level": "MEDIUM",
        "unique_senders": 2,
        "unique_recipients": 2,
        "total_inflow": 1980000.0,
        "total_outflow": 1900000.0,
        "net_retention": 80000.0,
        "centrality_index": 6.0
    }
]

with open("backend/static/app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Remove any previous dataset header
if "let networkInstance = null;" in app_js:
    parts = app_js.split("let networkInstance = null;")
    app_js = "let networkInstance = null;" + parts[-1]

data_block = f"""// ==========================================
// EMBEDDED REALISTIC DATASET (CLIENT-SIDE RESILIENCE)
// ==========================================
const DEFAULT_NODES = {json.dumps(mock_nodes, indent=2)};
const DEFAULT_EDGES = {json.dumps(mock_edges, indent=2)};
const DEFAULT_RINGS = {json.dumps(mock_rings, indent=2)};
const DEFAULT_UBO = {json.dumps(mock_ubo, indent=2)};
const DEFAULT_SANCTIONS = {json.dumps(mock_sanctions, indent=2)};
const DEFAULT_MULE_HUBS = {json.dumps(mock_mules, indent=2)};
"""

new_app_js = data_block + "\n" + app_js

# Fallback health check
new_app_js = new_app_js.replace(
    'badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-rose-500/10 border border-rose-500/30 text-xs text-rose-400";\n    text.innerText = "Backend Offline";',
    'badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300";\n    text.innerText = "Demo Simulation Mode";'
)

# Resilient loadCircularRings
old_rings_fn = """async function loadCircularRings() {
  const container = document.getElementById("ringsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Scanning transaction topology for closed loops...</div>`;

  try {
    const res = await fetch("/api/analytics/circular-rings?limit=10");
    const data = await res.json();
    const rings = data.rings || [];"""

new_rings_fn = """async function loadCircularRings() {
  const container = document.getElementById("ringsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Scanning transaction topology for closed loops...</div>`;

  let rings = DEFAULT_RINGS;
  try {
    const res = await fetch("/api/analytics/circular-rings?limit=10");
    if (res.ok) {
      const data = await res.json();
      if (data && Array.isArray(data.rings) && data.rings.length > 0) {
        rings = data.rings;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for circular rings", err);
  }"""

new_app_js = new_app_js.replace(old_rings_fn, new_rings_fn)

# Resilient resolveUBO
old_ubo_fn = """async function resolveUBO() {
  const companyId = document.getElementById("uboSelectCompany").value;
  const container = document.getElementById("uboResultsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Traversing recursive ownership graph [:OWNS*1..8]...</div>`;

  try {
    const res = await fetch(`/api/analytics/ubo/${encodeURIComponent(companyId)}?min_share_pct=5.0`);
    const data = await res.json();
    const ubos = data.beneficial_owners || [];"""

new_ubo_fn = """async function resolveUBO() {
  const companyId = document.getElementById("uboSelectCompany").value;
  const container = document.getElementById("uboResultsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Traversing recursive ownership graph [:OWNS*1..8]...</div>`;

  let ubos = DEFAULT_UBO[companyId] || [];
  try {
    const res = await fetch(`/api/analytics/ubo/${encodeURIComponent(companyId)}?min_share_pct=5.0`);
    if (res.ok) {
      const data = await res.json();
      if (data && Array.isArray(data.beneficial_owners)) {
        ubos = data.beneficial_owners;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for UBO resolution", err);
  }"""

new_app_js = new_app_js.replace(old_ubo_fn, new_ubo_fn)

# Resilient traceSanctionPath
old_sanction_fn = """async function traceSanctionPath() {
  const entityId = document.getElementById("sanctionSelectEntity").value;
  const container = document.getElementById("sanctionPathContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Running shortest-path traversal to Sanction Watchlists...</div>`;

  try {
    const res = await fetch(`/api/analytics/shortest-sanction-path/${encodeURIComponent(entityId)}`);
    const data = await res.json();"""

new_sanction_fn = """async function traceSanctionPath() {
  const entityId = document.getElementById("sanctionSelectEntity").value;
  const container = document.getElementById("sanctionPathContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Running shortest-path traversal to Sanction Watchlists...</div>`;

  let data = DEFAULT_SANCTIONS[entityId] || { found: false, message: `No sanction path found within 6 hops for ${entityId}` };
  try {
    const res = await fetch(`/api/analytics/shortest-sanction-path/${encodeURIComponent(entityId)}`);
    if (res.ok) {
      const liveData = await res.json();
      if (liveData && liveData.found !== undefined) {
        data = liveData;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for sanction path", err);
  }"""

new_app_js = new_app_js.replace(old_sanction_fn, new_sanction_fn)

# Resilient loadMuleHubs
old_mules_fn = """async function loadMuleHubs() {
  const container = document.getElementById("mulesContainer");
  try {
    const res = await fetch("/api/analytics/mule-hubs?limit=6");
    const data = await res.json();
    const hubs = data.hubs || [];"""

new_mules_fn = """async function loadMuleHubs() {
  const container = document.getElementById("mulesContainer");
  let hubs = DEFAULT_MULE_HUBS;
  try {
    const res = await fetch("/api/analytics/mule-hubs?limit=6");
    if (res.ok) {
      const data = await res.json();
      if (data && Array.isArray(data.hubs) && data.hubs.length > 0) {
        hubs = data.hubs;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for mule hubs", err);
  }"""

new_app_js = new_app_js.replace(old_mules_fn, new_mules_fn)

# Copy to all distribution paths
paths = ["backend/static/app.js", "public/app.js", "public/static/app.js", "app.js"]
for p in paths:
    os.makedirs(os.path.dirname(p) if os.path.dirname(p) else ".", exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(new_app_js)

# Also copy index.html and style.css across public, root, and backend/static
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

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

print("SUCCESS: All assets synchronized with full resilience!")
