/**
 * SentinelGraph - Frontend Application Controller
 * Handles Vis.js Canvas, API calls, AML modules, UBO Trees, and Cypher Console.
 */

let networkInstance = null;
let graphData = { nodes: [], edges: [] };
let rawNodes = [];
let rawEdges = [];
let visNodesDataSet = null;
let visEdgesDataSet = null;

// Initialize when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  if (window.lucide) {
    lucide.createIcons();
  }
  checkDatabaseHealth();
  loadMetrics();
  loadInitialGraph();
  setupSearch();
  loadCircularRings();
  loadMuleHubs();
});

// ==========================================
// 1. HEALTH & METRICS
// ==========================================
async function checkDatabaseHealth() {
  const badge = document.getElementById("dbStatusBadge");
  const text = document.getElementById("dbStatusText");
  try {
    const res = await fetch("/api/admin/health");
    const data = await res.json();
    if (data.database.connected) {
      badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-xs text-emerald-400";
      text.innerText = "CognoDB Cloud (Connected)";
    } else {
      badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300";
      text.innerText = "Demo Simulation Mode";
    }
  } catch (err) {
    badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-rose-500/10 border border-rose-500/30 text-xs text-rose-400";
    text.innerText = "Backend Offline";
  }
}

async function loadMetrics() {
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
}

// ==========================================
// 2. GRAPH CANVAS RENDERING (Vis.js)
// ==========================================
async function loadInitialGraph(nodeType = "", minRisk = 0.0) {
  const container = document.getElementById("graphCanvas");
  let url = `/api/graph/subgraph?`;
  if (nodeType) url += `node_type=${encodeURIComponent(nodeType)}&`;
  if (minRisk > 0) url += `min_risk=${minRisk}&`;

  try {
    const res = await fetch(url);
    const data = await res.json();
    rawNodes = data.nodes || [];
    rawEdges = data.edges || [];

    const nodesArray = rawNodes.map((n) => {
      const label = n.label || "Entity";
      const name = n.name || n.id;
      const risk = n.risk_score || 0.0;
      
      let color = { background: "#1e293b", border: "#64748b", highlight: { background: "#334155", border: "#38bdf8" } };
      let shape = "dot";
      let size = 20;

      if (label === "Person") {
        color = { background: "#0891b2", border: "#22d3ee", highlight: { background: "#06b6d4", border: "#a5f3fc" } };
        shape = "dot";
        size = 22;
      } else if (label === "Company") {
        color = { background: "#d97706", border: "#fbbf24", highlight: { background: "#f59e0b", border: "#fde68a" } };
        shape = "box";
        size = 24;
      } else if (label === "BankAccount") {
        color = { background: "#059669", border: "#34d399", highlight: { background: "#10b981", border: "#a7f3d0" } };
        shape = "ellipse";
        size = 18;
      } else if (label === "SanctionList") {
        color = { background: "#b91c1c", border: "#f87171", highlight: { background: "#ef4444", border: "#fca5a5" } };
        shape = "hexagon";
        size = 28;
      } else if (label === "Jurisdiction") {
        color = { background: "#7c3aed", border: "#c084fc", highlight: { background: "#8b5cf6", border: "#e9d5ff" } };
        shape = "diamond";
        size = 20;
      }

      // High-risk halo
      if (risk >= 0.8) {
        color.border = "#ef4444";
      }

      return {
        id: n.id,
        label: name.length > 22 ? name.substring(0, 20) + "..." : name,
        title: `${label}: ${name}\nRisk Score: ${(risk * 100).toFixed(0)}%`,
        shape: shape,
        size: size,
        color: color,
        font: { color: "#f8fafc", face: "Plus Jakarta Sans", size: 11 },
        borderWidth: risk >= 0.8 ? 3 : 1.5,
        rawNode: n
      };
    });

    const edgesArray = rawEdges.map((e, idx) => {
      let color = "#475569";
      let arrows = "to";
      let labelText = e.type;

      if (e.type === "TRANSFERRED_TO") {
        color = e.properties && e.properties.risk_flag ? "#ef4444" : "#10b981";
        const amt = e.properties && e.properties.amount ? `$${(e.properties.amount / 1000).toFixed(0)}k` : "";
        labelText = amt ? `TX ${amt}` : "TRANSFERRED_TO";
      } else if (e.type === "OWNS") {
        color = "#f59e0b";
        const pct = e.properties && e.properties.share_pct ? `${e.properties.share_pct}%` : "";
        labelText = pct ? `OWNS (${pct})` : "OWNS";
      } else if (e.type === "SANCTIONED_UNDER") {
        color = "#dc2626";
        labelText = "SANCTIONED";
      }

      return {
        id: e.id || `edge-${idx}`,
        from: e.source,
        to: e.target,
        label: labelText,
        color: { color: color, highlight: "#38bdf8" },
        font: { color: "#94a3b8", size: 9, face: "Plus Jakarta Sans", align: "middle", background: "#0b0f19" },
        arrows: { to: { enabled: true, scaleFactor: 0.8 } },
        smooth: { type: "curvedCW", roundness: 0.15 },
        rawEdge: e
      };
    });

    visNodesDataSet = new vis.DataSet(nodesArray);
    visEdgesDataSet = new vis.DataSet(edgesArray);

    const options = {
      nodes: {
        shadow: { enabled: true, color: "rgba(0,0,0,0.5)", size: 10, x: 2, y: 2 }
      },
      edges: {
        width: 1.5,
        selectionWidth: 3,
        shadow: { enabled: false }
      },
      physics: {
        enabled: true,
        solver: "forceAtlas2Based",
        forceAtlas2Based: {
          gravitationalConstant: -70,
          centralGravity: 0.015,
          springLength: 140,
          springConstant: 0.08,
          damping: 0.4
        },
        stabilization: { iterations: 120 }
      },
      interaction: {
        hover: true,
        tooltipDelay: 100,
        navigationButtons: false,
        keyboard: true
      }
    };

    if (networkInstance) {
      networkInstance.destroy();
    }

    networkInstance = new vis.Network(container, { nodes: visNodesDataSet, edges: visEdgesDataSet }, options);

    // Node click handler
    networkInstance.on("click", (params) => {
      if (params.nodes.length > 0) {
        const selectedId = params.nodes[0];
        const nodeItem = nodesArray.find((n) => n.id === selectedId);
        if (nodeItem) {
          openDrawer(nodeItem.rawNode);
        }
      }
    });

  } catch (err) {
    console.error("Failed to render graph canvas", err);
  }
}

function applyGraphFilters() {
  const nodeType = document.getElementById("filterNodeType").value;
  const minRisk = parseFloat(document.getElementById("filterMinRisk").value || "0.0");
  loadInitialGraph(nodeType, minRisk);
}

function togglePhysics(enabled) {
  if (networkInstance) {
    networkInstance.setOptions({ physics: { enabled: enabled } });
  }
}

function focusEntityOnCanvas(entityId) {
  switchTab("explorer");
  setTimeout(() => {
    if (networkInstance) {
      networkInstance.selectNodes([entityId]);
      networkInstance.focus(entityId, {
        scale: 1.3,
        animation: { duration: 800, easingFunction: "easeInOutQuad" }
      });
      const node = rawNodes.find((n) => (n.id === entityId || n.account_number === entityId));
      if (node) openDrawer(node);
    }
  }, 100);
}

// ==========================================
// 3. TAB NAVIGATION
// ==========================================
function switchTab(tabId) {
  document.querySelectorAll(".tab-btn").forEach((btn) => btn.classList.remove("active"));
  document.querySelectorAll(".view-panel").forEach((p) => p.classList.add("hidden"));

  const targetBtn = document.getElementById(`tab-${tabId}`);
  const targetView = document.getElementById(`view-${tabId}`);

  if (targetBtn) targetBtn.classList.add("active");
  if (targetView) targetView.classList.remove("hidden");

  if (window.lucide) lucide.createIcons();
}

// ==========================================
// 4. ENTITY 360 DRAWER
// ==========================================
function openDrawer(node) {
  const drawer = document.getElementById("entityDrawer");
  const content = document.getElementById("drawerContent");
  drawer.classList.remove("hidden");

  const label = node.label || "Entity";
  const name = node.name || node.id;
  const risk = (node.risk_score || node.base_risk || 0.0);
  const riskPercent = Math.round(risk * 100);
  const nid = node.id || node.account_number;

  let riskColor = "text-emerald-400 border-emerald-500/30 bg-emerald-500/10";
  if (riskPercent >= 75) riskColor = "text-crimson-500 border-crimson-500/30 bg-crimson-500/10";
  else if (riskPercent >= 40) riskColor = "text-amber-400 border-amber-500/30 bg-amber-500/10";

  let propHtml = "";
  const props = node.properties || node;
  for (const [k, v] of Object.entries(props)) {
    if (k === "properties" || k === "rawNode" || typeof v === "object") continue;
    propHtml += `
      <div class="flex justify-between py-1.5 border-b border-dark-700/50">
        <span class="text-slate-400 capitalize font-medium">${k.replace('_', ' ')}</span>
        <span class="text-slate-200 font-mono text-right truncate max-w-[180px]">${v}</span>
      </div>
    `;
  }

  content.innerHTML = `
    <div>
      <div class="flex items-start justify-between">
        <div>
          <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-dark-700 text-cyan-400 border border-dark-600">${label}</span>
          <h4 class="text-base font-bold text-white mt-1">${name}</h4>
          <p class="text-xs text-slate-400 font-mono">${nid}</p>
        </div>
        <div class="px-2.5 py-1 rounded-lg border font-bold font-mono text-xs ${riskColor}">
          Risk: ${riskPercent}%
        </div>
      </div>
    </div>

    <!-- Actions -->
    <div class="grid grid-cols-2 gap-2 pt-2">
      <button onclick="expandNeighborhood('${nid}')" class="flex items-center justify-center space-x-1.5 px-3 py-2 rounded-lg bg-dark-700 hover:bg-dark-600 border border-dark-600 text-slate-200 text-xs font-semibold transition-all">
        <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span>2-Hop Scope</span>
      </button>
      <button onclick="traceEntitySanctions('${nid}')" class="flex items-center justify-center space-x-1.5 px-3 py-2 rounded-lg bg-crimson-600/20 hover:bg-crimson-600/30 border border-crimson-500/30 text-crimson-400 text-xs font-semibold transition-all">
        <i data-lucide="shield-alert" class="w-3.5 h-3.5"></i>
        <span>Sanctions Trace</span>
      </button>
    </div>

    <!-- Properties -->
    <div class="bg-dark-900/60 rounded-xl p-3 border border-dark-700 space-y-1">
      <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">Entity Metadata</div>
      ${propHtml}
    </div>
  `;

  if (window.lucide) lucide.createIcons();
}

function closeDrawer() {
  document.getElementById("entityDrawer").classList.add("hidden");
}

async function expandNeighborhood(entityId) {
  try {
    const res = await fetch(`/api/graph/neighborhood/${encodeURIComponent(entityId)}`);
    const data = await res.json();
    showToast(`Loaded ${data.nodes.length} nodes in 2-hop neighborhood of ${entityId}`);
    focusEntityOnCanvas(entityId);
  } catch (err) {
    showToast(`Failed to expand neighborhood: ${err}`, true);
  }
}

function traceEntitySanctions(entityId) {
  switchTab("sanctions");
  const select = document.getElementById("sanctionSelectEntity");
  // Check if option exists, otherwise add it
  let exists = false;
  for (let i = 0; i < select.options.length; i++) {
    if (select.options[i].value === entityId) {
      select.selectedIndex = i;
      exists = true;
      break;
    }
  }
  if (!exists) {
    const opt = document.createElement("option");
    opt.value = entityId;
    opt.innerText = entityId;
    select.appendChild(opt);
    select.value = entityId;
  }
  traceSanctionPath();
}

// ==========================================
// 5. SMURFING RINGS (CIRCULAR CYCLES)
// ==========================================
async function loadCircularRings() {
  const container = document.getElementById("ringsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Scanning transaction topology for closed loops...</div>`;

  try {
    const res = await fetch("/api/analytics/circular-rings?limit=10");
    const data = await res.json();
    const rings = data.rings || [];

    if (rings.length === 0) {
      container.innerHTML = `<div class="p-8 text-center text-slate-400 text-xs">No circular loops detected.</div>`;
      return;
    }

    container.innerHTML = rings.map((ring, idx) => {
      const vol = (ring.total_volume || 0).toLocaleString("en-US", { style: "currency", currency: "USD" });
      const nodes = ring.ring_nodes || [];
      const edges = ring.ring_edges || [];

      const chainHtml = ring.account_chain.map((acc, i) => `
        <span class="px-2 py-1 rounded bg-dark-900 text-cyan-300 font-mono text-xs border border-dark-600">${acc}</span>
        ${i < ring.account_chain.length - 1 ? `<i data-lucide="arrow-right" class="w-3.5 h-3.5 text-amber-400"></i>` : ''}
      `).join('');

      return `
        <div class="intel-card bg-dark-800 border border-amber-500/30 rounded-xl p-5 space-y-4 shadow-xl">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-700 pb-3">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-xs">#${idx + 1}</div>
              <div>
                <h4 class="font-bold text-sm text-white">Circular Smurfing Ring (${ring.loop_length} Hops)</h4>
                <p class="text-xs text-slate-400">Origin Bank: <span class="text-slate-200 font-semibold">${ring.origin_bank}</span> (${ring.origin_account})</p>
              </div>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">Laundered Loop Volume</div>
              <div class="text-base font-extrabold text-amber-400 font-mono">${vol}</div>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-2 py-1 bg-dark-900/60 p-3 rounded-lg border border-dark-700/60">
            ${chainHtml}
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="bg-dark-900/40 p-3 rounded-lg border border-dark-700 space-y-1.5">
              <div class="font-bold text-slate-400 uppercase text-[10px]">Involved Accounts</div>
              ${nodes.map(n => `
                <div class="flex justify-between items-center py-0.5">
                  <span class="text-slate-300">${n.bank_name || n.account_number}</span>
                  <span class="font-mono text-[11px] px-1.5 rounded bg-dark-700 text-amber-300">${n.country || 'Offshore'}</span>
                </div>
              `).join('')}
            </div>

            <div class="bg-dark-900/40 p-3 rounded-lg border border-dark-700 space-y-1.5">
              <div class="font-bold text-slate-400 uppercase text-[10px]">Transaction Hops</div>
              ${edges.map(e => `
                <div class="flex justify-between items-center py-0.5 font-mono text-[11px]">
                  <span class="text-cyan-400">${e.tx_id}</span>
                  <span class="text-emerald-400 font-bold">$${(e.amount).toLocaleString()} ${e.currency}</span>
                </div>
              `).join('')}
            </div>
          </div>

          <div class="flex justify-end pt-1">
            <button onclick="focusEntityOnCanvas('${ring.origin_account}')" class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-dark-700 hover:bg-dark-600 text-cyan-400 font-semibold text-xs border border-dark-600 transition-all">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>Locate in Network Canvas</span>
            </button>
          </div>
        </div>
      `;
    }).join("");

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<div class="p-4 text-rose-400 text-xs">Failed to load circular rings: ${err}</div>`;
  }
}

// ==========================================
// 6. UBO RESOLUTION (MULTI-TIER OWNERSHIP)
// ==========================================
async function resolveUBO() {
  const companyId = document.getElementById("uboSelectCompany").value;
  const container = document.getElementById("uboResultsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Traversing recursive ownership graph [:OWNS*1..8]...</div>`;

  try {
    const res = await fetch(`/api/analytics/ubo/${encodeURIComponent(companyId)}?min_share_pct=5.0`);
    const data = await res.json();
    const ubos = data.beneficial_owners || [];

    if (ubos.length === 0) {
      container.innerHTML = `<div class="bg-dark-800 border border-dark-700 rounded-xl p-6 text-center text-slate-400 text-xs">No beneficial owners found for this company.</div>`;
      return;
    }

    container.innerHTML = ubos.map((ubo, idx) => {
      const effPct = ubo.effective_ownership_pct;
      const isControl = effPct >= 25.0;
      const chainNodes = ubo.ownership_chain || [];
      const relChain = ubo.relationship_chain || [];

      return `
        <div class="intel-card bg-dark-800 border ${isControl ? 'border-emerald-500/40' : 'border-dark-700'} rounded-xl p-5 space-y-4 shadow-xl">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-700 pb-3">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-lg ${ubo.is_pep ? 'bg-crimson-500/20 text-crimson-400' : 'bg-emerald-500/20 text-emerald-400'} flex items-center justify-center font-bold text-sm">
                <i data-lucide="user-check" class="w-5 h-5"></i>
              </div>
              <div>
                <div class="flex items-center space-x-2">
                  <h4 class="font-bold text-base text-white">${ubo.ubo_name}</h4>
                  ${ubo.is_pep ? `<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-crimson-500/20 text-crimson-400 border border-crimson-500/30">PEP EXPOSURE</span>` : ''}
                </div>
                <p class="text-xs text-slate-400">Nationality: <span class="text-slate-200 font-semibold">${ubo.nationality}</span> | UBO Depth: <span class="text-emerald-400 font-bold">${ubo.ownership_depth} Layers</span></p>
              </div>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">Calculated Effective Share</div>
              <div class="text-xl font-extrabold ${isControl ? 'text-emerald-400' : 'text-slate-200'} font-mono">${effPct}%</div>
            </div>
          </div>

          <!-- Visual Ownership Pathway -->
          <div class="space-y-2">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Multi-Tier Ownership Chain</div>
            <div class="bg-dark-900/60 p-4 rounded-xl border border-dark-700/80 space-y-3">
              ${chainNodes.map((n, i) => {
                const rel = relChain[i];
                return `
                  <div class="flex items-center space-x-3">
                    <div class="w-6 h-6 rounded-full bg-dark-700 text-cyan-400 flex items-center justify-center font-bold text-[10px] shrink-0">${i + 1}</div>
                    <div class="flex-1 bg-dark-800 p-2.5 rounded-lg border border-dark-600/80 flex items-center justify-between">
                      <div>
                        <div class="font-bold text-xs text-slate-200">${n.name}</div>
                        <div class="text-[10px] text-slate-400">${n.type} • ${n.jurisdiction}</div>
                      </div>
                      <div class="text-right">
                        ${rel ? `<span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Owns ${rel.share_pct}%</span>` : `<span class="text-xs text-slate-400">Target Asset</span>`}
                      </div>
                    </div>
                  </div>
                  ${i < chainNodes.length - 1 ? `<div class="pl-3 py-0.5"><i data-lucide="arrow-down" class="w-3.5 h-3.5 text-emerald-400"></i></div>` : ''}
                `;
              }).join('')}
            </div>
          </div>

          <div class="flex justify-end pt-1">
            <button onclick="focusEntityOnCanvas('${ubo.ubo_id}')" class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-dark-700 hover:bg-dark-600 text-cyan-400 font-semibold text-xs border border-dark-600 transition-all">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>Locate UBO in Canvas</span>
            </button>
          </div>
        </div>
      `;
    }).join("");

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<div class="p-4 text-rose-400 text-xs">Failed to compute UBO: ${err}</div>`;
  }
}

// ==========================================
// 7. SANCTIONS PATH TRACER
// ==========================================
async function traceSanctionPath() {
  const entityId = document.getElementById("sanctionSelectEntity").value;
  const container = document.getElementById("sanctionPathContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Running shortest-path traversal to Sanction Watchlists...</div>`;

  try {
    const res = await fetch(`/api/analytics/shortest-sanction-path/${encodeURIComponent(entityId)}`);
    const data = await res.json();

    if (!data.found) {
      container.innerHTML = `
        <div class="bg-dark-800 border border-dark-700 rounded-xl p-6 text-center space-y-2">
          <i data-lucide="shield-check" class="w-8 h-8 text-emerald-400 mx-auto"></i>
          <h4 class="font-bold text-sm text-white">No Sanction Exposure Detected</h4>
          <p class="text-xs text-slate-400">${data.message || 'No connection found within 6 hops.'}</p>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    const path = data.path;
    const nodes = path.path_nodes || [];
    const rels = path.path_relationships || [];

    container.innerHTML = `
      <div class="intel-card bg-dark-800 border border-crimson-500/40 rounded-xl p-5 space-y-4 shadow-xl">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-700 pb-3">
          <div class="flex items-center space-x-3">
            <div class="w-9 h-9 rounded-lg bg-crimson-500/20 text-crimson-400 flex items-center justify-center font-bold text-sm">
              <i data-lucide="alert-triangle" class="w-5 h-5"></i>
            </div>
            <div>
              <h4 class="font-bold text-base text-white">Direct / Indirect Sanctions Exposure</h4>
              <p class="text-xs text-slate-400">Target List: <span class="text-crimson-400 font-bold">${path.sanction_program}</span> (${path.sanctioning_body})</p>
            </div>
          </div>
          <div class="text-right">
            <div class="text-xs text-slate-400">Graph Distance</div>
            <div class="text-xl font-extrabold text-crimson-400 font-mono">${path.distance} Hops</div>
          </div>
        </div>

        <div class="bg-crimson-950/20 border border-crimson-500/30 rounded-lg p-3 text-xs text-slate-300">
          <span class="font-bold text-crimson-400 uppercase text-[10px] block mb-1">Sanction Justification</span>
          ${path.sanction_reason}
        </div>

        <!-- Step by Step Chain -->
        <div class="space-y-2">
          <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Tainted Capital Pathway</div>
          <div class="bg-dark-900/60 p-4 rounded-xl border border-dark-700/80 space-y-3">
            ${nodes.map((n, i) => {
              const rel = rels[i];
              return `
                <div class="flex items-center space-x-3">
                  <div class="w-6 h-6 rounded-full bg-dark-700 text-crimson-400 flex items-center justify-center font-bold text-[10px] shrink-0">${i + 1}</div>
                  <div class="flex-1 bg-dark-800 p-2.5 rounded-lg border border-dark-600/80 flex items-center justify-between">
                    <div>
                      <div class="font-bold text-xs text-slate-200">${n.name}</div>
                      <div class="text-[10px] text-slate-400">${n.label} • ${n.country}</div>
                    </div>
                    <div class="text-right">
                      ${rel ? `<span class="px-2 py-0.5 rounded bg-dark-700 text-cyan-300 font-mono text-[10px]">${rel.type}</span>` : `<span class="px-2 py-0.5 rounded bg-crimson-500/20 text-crimson-400 font-mono text-[10px] font-bold">SANCTION NODE</span>`}
                    </div>
                  </div>
                </div>
                ${i < nodes.length - 1 ? `<div class="pl-3 py-0.5"><i data-lucide="arrow-down" class="w-3.5 h-3.5 text-crimson-400"></i></div>` : ''}
              `;
            }).join('')}
          </div>
        </div>
      </div>
    `;

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<div class="p-4 text-rose-400 text-xs">Failed to trace sanctions path: ${err}</div>`;
  }
}

// ==========================================
// 8. MULE TRANSIT HUBS
// ==========================================
async function loadMuleHubs() {
  const container = document.getElementById("mulesContainer");
  try {
    const res = await fetch("/api/analytics/mule-hubs?limit=6");
    const data = await res.json();
    const hubs = data.hubs || [];

    container.innerHTML = hubs.map((h) => `
      <div class="intel-card bg-dark-800 border border-purple-500/30 rounded-xl p-4 space-y-3 shadow-xl">
        <div class="flex items-center justify-between border-b border-dark-700 pb-2">
          <div>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 font-mono">TRANSIT NEXUS</span>
            <h4 class="font-bold text-sm text-white mt-1">${h.bank_name}</h4>
            <p class="text-xs text-slate-400 font-mono">${h.account_number} (${h.country})</p>
          </div>
          <div class="text-right">
            <div class="text-[10px] text-slate-400">Centrality Index</div>
            <div class="text-base font-extrabold text-purple-400 font-mono">${h.centrality_index}</div>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-2 text-center text-xs">
          <div class="bg-dark-900/60 p-2 rounded-lg border border-dark-700">
            <div class="text-[10px] text-slate-400">Total Inflow</div>
            <div class="font-bold text-emerald-400 font-mono text-[11px]">$${(h.total_inflow).toLocaleString()}</div>
          </div>
          <div class="bg-dark-900/60 p-2 rounded-lg border border-dark-700">
            <div class="text-[10px] text-slate-400">Total Outflow</div>
            <div class="font-bold text-rose-400 font-mono text-[11px]">$${(h.total_outflow).toLocaleString()}</div>
          </div>
          <div class="bg-dark-900/60 p-2 rounded-lg border border-dark-700">
            <div class="text-[10px] text-slate-400">Retained Net</div>
            <div class="font-bold text-slate-200 font-mono text-[11px]">$${(h.net_retention).toLocaleString()}</div>
          </div>
        </div>

        <div class="flex justify-end pt-1">
          <button onclick="focusEntityOnCanvas('${h.account_number}')" class="text-xs text-cyan-400 hover:underline flex items-center space-x-1">
            <span>Inspect in Canvas</span>
            <i data-lucide="chevron-right" class="w-3 h-3"></i>
          </button>
        </div>
      </div>
    `).join("");

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    console.error("Failed to load mules", err);
  }
}

// ==========================================
// 9. CYPHER QUERY PLAYGROUND
// ==========================================
const CYPHER_PRESETS = {
  1: `MATCH path = (origin:BankAccount)-[txs:TRANSFERRED_TO*3..6]->(origin)
RETURN origin.account_number AS origin_acc, length(path) AS hops,
       reduce(s = 0, t IN txs | s + t.amount) AS volume
ORDER BY volume DESC LIMIT 5`,
  2: `MATCH path = (root:Person)-[owns:OWNS*1..8]->(target:Company {id: 'C-208'})
RETURN root.name AS ubo, root.nationality AS nationality,
       reduce(pct = 1.0, r IN owns | pct * (r.share_pct/100.0)) * 100.0 AS effective_pct,
       length(path) AS depth`,
  3: `MATCH (start:Company {id: 'C-208'}), (sanction:SanctionList)
MATCH p = shortestPath((start)-[*1..6]-(sanction))
RETURN length(p) AS hops, [n IN nodes(p) | coalesce(n.name, n.account_number)] AS entity_trail`,
  4: `MATCH (c:Company)-[:REGISTERED_IN]->(j:Jurisdiction {tax_haven: true})
OPTIONAL MATCH (p:Person)-[o:OWNS]->(c)
RETURN c.name AS company, j.name AS haven, p.name AS owner, o.share_pct AS share`
};

function setCypherPreset(num) {
  const query = CYPHER_PRESETS[num] || "";
  document.getElementById("cypherInput").value = query;
}

async function runCustomCypher() {
  const query = document.getElementById("cypherInput").value.trim();
  const output = document.getElementById("cypherOutput");
  const stats = document.getElementById("cypherExecStats");

  if (!query) {
    output.innerText = "Please enter a Cypher query.";
    return;
  }

  output.innerText = "Executing Cypher against CognoDB Cloud...";
  stats.innerText = "Query in flight...";

  try {
    const res = await fetch("/api/analytics/cypher-console", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query, parameters: {} })
    });
    const data = await res.json();

    if (data.success) {
      stats.innerText = `Success | ${data.row_count} records returned in ${data.execution_time_ms} ms (${data.mode})`;
      output.innerText = JSON.stringify(data.data, null, 2);
    } else {
      stats.innerText = `Query Error (${data.mode})`;
      output.innerText = data.error || "An error occurred executing query.";
    }
  } catch (err) {
    stats.innerText = "Execution failed";
    output.innerText = `Network/Server Error: ${err}`;
  }
}

// ==========================================
// 10. GLOBAL SEARCH & SEEDING UTILITIES
// ==========================================
function setupSearch() {
  const input = document.getElementById("globalSearchInput");
  const dropdown = document.getElementById("searchResultsDropdown");
  let debounceTimeout = null;

  input.addEventListener("input", () => {
    clearTimeout(debounceTimeout);
    const term = input.value.trim();
    if (term.length < 2) {
      dropdown.classList.add("hidden");
      return;
    }

    debounceTimeout = setTimeout(async () => {
      try {
        const res = await fetch(`/api/search/?q=${encodeURIComponent(term)}`);
        const data = await res.json();
        const results = data.results || [];

        if (results.length === 0) {
          dropdown.innerHTML = `<div class="p-3 text-slate-400 text-xs">No matching entities found.</div>`;
          dropdown.classList.remove("hidden");
          return;
        }

        dropdown.innerHTML = results.map((r) => `
          <div onclick="focusEntityOnCanvas('${r.id}'); document.getElementById('searchResultsDropdown').classList.add('hidden');" class="p-2.5 hover:bg-dark-700 cursor-pointer flex items-center justify-between text-xs transition-colors">
            <div>
              <div class="font-bold text-slate-200">${r.name}</div>
              <div class="text-[10px] text-slate-400">${r.label} • ${r.country || 'N/A'}</div>
            </div>
            <span class="px-2 py-0.5 rounded font-mono text-[10px] ${r.risk_score >= 0.7 ? 'bg-crimson-500/20 text-crimson-400' : 'bg-dark-600 text-slate-300'}">
              ${(r.risk_score * 100).toFixed(0)}%
            </span>
          </div>
        `).join("");

        dropdown.classList.remove("hidden");
      } catch (e) {
        console.error("Search error", e);
      }
    }, 250);
  });

  document.addEventListener("click", (e) => {
    if (!input.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.add("hidden");
    }
  });
}

async function triggerSeed() {
  if (!confirm("This will ingest the SentinelGraph syndicate dataset into your live CognoDB Cloud instance. Continue?")) {
    return;
  }
  showToast("Seeding dataset into CognoDB...");
  try {
    const res = await fetch("/api/admin/seed?clear_first=true", { method: "POST" });
    const data = await res.json();
    if (data.success) {
      showToast(`Successfully seeded ${data.nodes_inserted} nodes and ${data.relationships_inserted} relationships!`);
      loadMetrics();
      loadInitialGraph();
      loadCircularRings();
      loadMuleHubs();
    } else {
      showToast(`Seed failed: ${data.detail || 'Check database connection'}`, true);
    }
  } catch (err) {
    showToast(`Seeding request error: ${err}`, true);
  }
}

function showToast(msg, isError = false) {
  const toast = document.getElementById("toast");
  const text = document.getElementById("toastMsg");
  text.innerText = msg;
  toast.className = isError
    ? "fixed bottom-5 right-5 z-50 px-4 py-3 rounded-xl bg-dark-800 border border-crimson-500/60 text-crimson-400 text-xs shadow-2xl flex items-center space-x-2 transition-all"
    : "fixed bottom-5 right-5 z-50 px-4 py-3 rounded-xl bg-dark-800 border border-emerald-500/60 text-emerald-400 text-xs shadow-2xl flex items-center space-x-2 transition-all";
  toast.classList.remove("hidden");
  setTimeout(() => toast.classList.add("hidden"), 4000);
}

function exportGraphImage() {
  if (!networkInstance) return;
  const canvas = document.querySelector("#graphCanvas canvas");
  if (canvas) {
    const link = document.createElement("a");
    link.download = "sentinelgraph-intelligence-canvas.png";
    link.href = canvas.toDataURL("image/png");
    link.click();
    showToast("Graph canvas exported as image.");
  }
}
