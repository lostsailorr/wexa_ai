import os

# 1. Update index.html
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add ID to stats ribbon if missing
if 'id="statsRibbon"' not in html:
    html = html.replace(
        '<div class="bg-dark-800/40 border-b border-dark-700/60 px-6 py-2.5 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4 text-xs">',
        '<div id="statsRibbon" class="bg-dark-800/40 border-b border-dark-700/60 px-6 py-2.5 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4 text-xs">'
    )

# Add ID to graph canvas container if missing
if 'id="graphCanvasContainer"' not in html:
    html = html.replace(
        '<div class="relative flex-1 bg-dark-900 overflow-hidden flex flex-col">',
        '<div id="graphCanvasContainer" class="relative flex-1 bg-dark-900 overflow-hidden flex flex-col">'
    )

# Remove any old walkthroughOverlay if exists
if '<div id="walkthroughOverlay"' in html:
    parts = html.split('<div id="walkthroughOverlay"')
    rest = parts[1].split('</body>')
    html = parts[0] + '</body>' + rest[1]

# Add Walkthrough button in header before Seed CognoDB button if not present
walkthrough_btn = '''      <!-- Walkthrough Tour Button -->
      <button 
        id="btnStartWalkthrough" 
        onclick="startWalkthrough()" 
        title="Start Interactive App Walkthrough"
        class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500/20 via-indigo-500/20 to-emerald-500/20 hover:from-cyan-500/30 hover:to-emerald-500/30 border border-cyan-500/40 text-cyan-300 text-xs font-bold transition-all hover:scale-[1.03] active:scale-[0.98] shadow-lg shadow-cyan-500/10"
      >
        <i data-lucide="compass" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span>Walkthrough</span>
      </button>

'''

if "btnStartWalkthrough" not in html:
    html = html.replace('<!-- Seed Database Button -->', walkthrough_btn + '      <!-- Seed Database Button -->')

# Add Polished Walkthrough Dock Modal (Bottom-Right Non-Overlapping)
tour_modal = '''
  <!-- GUIDED WALKTHROUGH OVERLAY & FLOATING DOCK -->
  <div id="walkthroughOverlay" class="hidden fixed inset-0 z-50 pointer-events-none transition-all duration-300">
    <div id="tourBackdrop" onclick="stopWalkthrough()" class="absolute inset-0 bg-dark-900/35 backdrop-blur-[2px] pointer-events-auto cursor-pointer"></div>
    
    <!-- Floating Bottom-Right Tour Guide Dock (Guaranteed Zero Overlap) -->
    <div id="tourCard" class="fixed bottom-6 right-6 pointer-events-auto max-w-md w-[420px] p-5 rounded-2xl bg-dark-800/95 border border-cyan-500/50 shadow-2xl shadow-cyan-500/20 backdrop-blur-xl transition-all duration-300 z-50">
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-3 mb-3">
        <div class="flex items-center space-x-2">
          <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
          <span id="tourStepBadge" class="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">Step 1 of 8</span>
        </div>
        
        <!-- Step Progress Dots -->
        <div id="tourDots" class="flex items-center space-x-1"></div>

        <button onclick="stopWalkthrough()" title="Close Walkthrough" class="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-dark-700 transition-colors">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-2">
        <h3 id="tourTitle" class="text-sm font-bold text-white flex items-center space-x-2">
          Tour Title
        </h3>
        <p id="tourDescription" class="text-xs text-slate-300 leading-relaxed">
          Tour Description
        </p>
      </div>

      <div class="flex items-center justify-between pt-3.5 mt-3.5 border-t border-dark-700/80">
        <button onclick="stopWalkthrough()" class="text-xs text-slate-400 hover:text-slate-200 transition-colors">
          Skip Tour
        </button>
        <div class="flex items-center space-x-2">
          <button id="tourPrevBtn" onclick="prevTourStep()" class="px-3 py-1.5 rounded-lg bg-dark-700 hover:bg-dark-600 text-xs font-semibold text-slate-200 transition-all border border-dark-600">
            Back
          </button>
          <button id="tourNextBtn" onclick="nextTourStep()" class="px-4 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500 to-cyan-400 hover:from-cyan-400 hover:to-cyan-300 text-dark-900 text-xs font-bold transition-all shadow-md shadow-cyan-500/20">
            Next →
          </button>
        </div>
      </div>
    </div>
  </div>
'''

html = html.replace('</body>', tour_modal + '\n</body>')

# 2. Update style.css
with open("backend/static/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove previous tour-highlight if present
if ".tour-highlight" in css:
    css = css.split("/* Tour Highlight")[0]

tour_css = '''
/* Tour Highlight & Spotlight Effects */
.tour-highlight {
  position: relative !important;
  z-index: 51 !important;
  box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.8), 0 0 25px rgba(6, 182, 212, 0.4) !important;
  border-color: rgba(6, 182, 212, 0.9) !important;
}
'''

css = css.strip() + "\n" + tour_css

# 3. Update app.js
with open("backend/static/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Remove previous walkthrough js if present
if "function startWalkthrough()" in js:
    js = js.split("// ==========================================\n// 8. INTERACTIVE GUIDED WALKTHROUGH")[0]

tour_js = '''
// ==========================================
// 8. INTERACTIVE GUIDED WALKTHROUGH
// ==========================================
let currentTourIndex = 0;
const tourSteps = [
  {
    targetId: "statsRibbon",
    title: "📊 Live Network Topology Telemetry",
    desc: "SentinelGraph continuously monitors network telemetry: 10 Persons, 11 Companies, 13 Bank Accounts, and 49 Relationships with live risk scores.",
    action: () => switchTab("explorer")
  },
  {
    targetId: "graphCanvasContainer",
    title: "🕸️ Force-Directed Network Canvas",
    desc: "Interactive Vis.js graph physics simulation. Nodes are color-coded (Cyan=Persons, Orange=Companies, Green=Accounts, Red=Sanctions). Click any node to open its 360° Risk Profile.",
    action: () => {
      switchTab("explorer");
      focusEntityOnCanvas("C-201");
    }
  },
  {
    targetId: "globalSearchInput",
    title: "🔍 Instant Entity Search & Autocomplete",
    desc: "Debounced live search across all suspect persons, offshore holding entities, bank account numbers, and sanction watchlists with instant camera focusing.",
    action: () => switchTab("explorer")
  },
  {
    targetId: "tab-rings",
    title: "🔄 Multi-Hop Smurfing Ring Detection",
    desc: "Uncovers obfuscated circular money laundering loops (3 to 6 hops deep) where capital routes through multi-jurisdiction intermediaries and returns to the originator.",
    action: () => switchTab("rings")
  },
  {
    targetId: "tab-ubo",
    title: "🏢 Recursive Ultimate Beneficial Ownership (UBO)",
    desc: "Traverses up to 8 hops deep across complex offshore shell holding chains (BVI, Cyprus, Panama) and computes cumulative effective ownership math using Cypher reduce().",
    action: () => {
      switchTab("ubo");
      resolveUBO();
    }
  },
  {
    targetId: "tab-sanctions",
    title: "🛡️ Shortest Path to Sanction Lists",
    desc: "Calculates the shortest relationship corridor connecting any suspect entity directly to OFAC SDN and EU watchlists in milliseconds.",
    action: () => {
      switchTab("sanctions");
      traceSanctionPath();
    }
  },
  {
    targetId: "tab-mules",
    title: "⚡ Mule Transit Hub & Centrality Detection",
    desc: "Identifies transit hub accounts exhibiting high transaction velocity, multiple incoming deposits, and rapid outgoing dispersal.",
    action: () => switchTab("mules")
  },
  {
    targetId: "tab-cypher",
    title: "💻 Live openCypher Query Console",
    desc: "Interactive Cypher playground for compliance investigators. Run custom or preset openCypher queries directly against CognoDB Cloud with live execution timing.",
    action: () => switchTab("cypher")
  }
];

function startWalkthrough() {
  currentTourIndex = 0;
  const overlay = document.getElementById("walkthroughOverlay");
  if (overlay) overlay.classList.remove("hidden");
  renderTourStep();
}

function stopWalkthrough() {
  const overlay = document.getElementById("walkthroughOverlay");
  if (overlay) overlay.classList.add("hidden");
  document.querySelectorAll(".tour-highlight").forEach(el => el.classList.remove("tour-highlight"));
}

function renderTourStep() {
  document.querySelectorAll(".tour-highlight").forEach(el => el.classList.remove("tour-highlight"));

  const step = tourSteps[currentTourIndex];
  if (!step) return;

  if (step.action) step.action();

  const badge = document.getElementById("tourStepBadge");
  const title = document.getElementById("tourTitle");
  const desc = document.getElementById("tourDescription");
  const prevBtn = document.getElementById("tourPrevBtn");
  const nextBtn = document.getElementById("tourNextBtn");
  const dotsContainer = document.getElementById("tourDots");

  if (badge) badge.innerText = `Step ${currentTourIndex + 1} of ${tourSteps.length}`;
  if (title) title.innerText = step.title;
  if (desc) desc.innerText = step.desc;

  if (prevBtn) prevBtn.style.visibility = currentTourIndex === 0 ? "hidden" : "visible";
  if (nextBtn) nextBtn.innerText = currentTourIndex === tourSteps.length - 1 ? "Finish Tour 🎉" : "Next →";

  // Render progress dots
  if (dotsContainer) {
    dotsContainer.innerHTML = tourSteps.map((_, i) => `
      <span class="w-1.5 h-1.5 rounded-full transition-all ${i === currentTourIndex ? 'bg-cyan-400 w-3' : 'bg-dark-600'}"></span>
    `).join('');
  }

  const targetEl = document.getElementById(step.targetId);
  if (targetEl) {
    targetEl.classList.add("tour-highlight");
    targetEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  if (window.lucide) lucide.createIcons();
}

function nextTourStep() {
  if (currentTourIndex < tourSteps.length - 1) {
    currentTourIndex++;
    renderTourStep();
  } else {
    stopWalkthrough();
    showToast("Walkthrough completed! Explore the graph freely.");
  }
}

function prevTourStep() {
  if (currentTourIndex > 0) {
    currentTourIndex--;
    renderTourStep();
  }
}
'''

js = js.strip() + "\n" + tour_js

# Write updated files across backend/static, public, and root
for folder in ["backend/static", "public", "public/static", "."]:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(folder, "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    with open(os.path.join(folder, "app.js"), "w", encoding="utf-8") as f:
        f.write(js)

print("Walkthrough floating dock and zero-overlap styling successfully updated!")
