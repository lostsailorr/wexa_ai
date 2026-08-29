import os

# 1. Update index.html
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Completely remove any backdrop-blur from tourBackdrop and walkthrough dock
# Make backdrop completely transparent (zero blur)
tour_overlay_html = '''  <!-- GUIDED WALKTHROUGH DOCK (ZERO BLUR, BLINKING MARKED MODULES) -->
  <div id="walkthroughOverlay" class="hidden fixed inset-0 z-50 pointer-events-none transition-all duration-300">
    <!-- Zero blur click-away backdrop -->
    <div id="tourBackdrop" onclick="stopWalkthrough()" class="absolute inset-0 bg-transparent pointer-events-auto cursor-pointer"></div>
    
    <!-- Floating Tour Guide Dock: Strict bottom-right positioning, zero overlap, solid crisp card -->
    <div id="tourCard" class="fixed bottom-6 right-6 pointer-events-auto max-w-md w-[420px] p-5 rounded-2xl bg-dark-800 border-2 border-cyan-500 shadow-2xl shadow-cyan-500/30 transition-all duration-300 z-50">'''

if '<div id="walkthroughOverlay"' in html:
    parts = html.split('<div id="walkthroughOverlay"')
    rest = parts[1].split('<div class="flex items-center justify-between border-b')
    html = parts[0] + tour_overlay_html + '\n      <div class="flex items-center justify-between border-b' + rest[1]

# 2. Update style.css
with open("backend/static/style.css", "r", encoding="utf-8") as f:
    css = f.read()

if "/* Tour Highlight" in css:
    css = css.split("/* Tour Highlight")[0]

tour_css = '''/* Tour Highlight & Spotlight Effects - Zero blur, prominent single blink animation */
.tour-highlight {
  position: relative !important;
  z-index: 60 !important;
  box-shadow: 0 0 0 3px #06b6d4, 0 0 25px rgba(6, 182, 212, 0.75) !important;
  border-color: #22d3ee !important;
  background-color: rgba(6, 182, 212, 0.25) !important;
  color: #ffffff !important;
  outline: 2px solid #38bdf8 !important;
  outline-offset: 2px !important;
  transition: all 0.25s ease-in-out !important;
}

@keyframes tourBlinkAnimation {
  0% {
    box-shadow: 0 0 0 0 rgba(6, 182, 212, 0);
    transform: scale(1);
    background-color: transparent;
  }
  25% {
    box-shadow: 0 0 0 8px #38bdf8, 0 0 45px rgba(56, 189, 248, 1);
    transform: scale(1.05);
    background-color: rgba(6, 182, 212, 0.45);
  }
  50% {
    box-shadow: 0 0 0 2px #06b6d4, 0 0 10px rgba(6, 182, 212, 0.3);
    transform: scale(1);
    background-color: rgba(6, 182, 212, 0.15);
  }
  75% {
    box-shadow: 0 0 0 8px #38bdf8, 0 0 45px rgba(56, 189, 248, 1);
    transform: scale(1.05);
    background-color: rgba(6, 182, 212, 0.45);
  }
  100% {
    box-shadow: 0 0 0 3px #06b6d4, 0 0 25px rgba(6, 182, 212, 0.75);
    transform: scale(1);
    background-color: rgba(6, 182, 212, 0.25);
  }
}

.tour-blink {
  animation: tourBlinkAnimation 0.85s cubic-bezier(0.2, 0.8, 0.2, 1) 1 forwards !important;
}
'''
css = css.strip() + "\n\n" + tour_css

# 3. Update app.js
with open("backend/static/app.js", "r", encoding="utf-8") as f:
    js = f.read()

walkthrough_section = '''// ==========================================
// 12. WALKTHROUGH TOUR ENGINE (ZERO BLUR, BLINKING MARKED MODULES)
// ==========================================
const TOUR_STEPS = [
  {
    tab: "explorer",
    targetId: "tab-explorer",
    title: "1. Global AML & Sanctions Network Canvas",
    description: "Interactive visual topology of high-risk oligarchs, front companies, offshore accounts, and sanctions watchlists."
  },
  {
    tab: "explorer",
    targetId: "view-controls",
    title: "2. Graph Filtering & Risk Sliders",
    description: "Filter by entity classes (e.g., Banks, PEPs, Shells) or dial minimum risk thresholds in real time."
  },
  {
    tab: "rings",
    targetId: "tab-rings",
    title: "3. Smurfing Rings & Circular Laundering",
    description: "Automated cycle detection scans for layered transaction loops (3-6 hops) routing money back to source."
  },
  {
    tab: "ubo",
    targetId: "tab-ubo",
    title: "4. Multi-Tier Ultimate Beneficial Ownership (UBO)",
    description: "Recursively unwinds complex holding company ownership paths to identify controlling PEPs and calculate effective ownership %."
  },
  {
    tab: "sanctions",
    targetId: "tab-sanctions",
    title: "5. Sanctions Evasion & Watchlist Tracer",
    description: "Computes shortest network paths connecting target companies directly to designated OFAC/EU sanctions lists."
  },
  {
    tab: "mules",
    targetId: "tab-mules",
    title: "6. Mule Transit Hub Centrality",
    description: "Detects intermediary mule bank accounts with rapid fund pass-through, high transaction velocity, and low retention."
  },
  {
    tab: "cypher",
    targetId: "tab-cypher",
    title: "7. Cypher Playground & Console",
    description: "Direct access to run native Cypher graph queries and export subgraphs with live query telemetry."
  },
  {
    tab: "explorer",
    targetId: "btnSeedDb",
    title: "8. Live CognoDB Integration",
    description: "Powered by CognoDB Cloud graph database for enterprise-grade real-time investigative intelligence. Click to seed syndicate data."
  }
];

let currentTourIndex = 0;

function startWalkthrough() {
  currentTourIndex = 0;
  const overlay = document.getElementById("walkthroughOverlay");
  if (overlay) overlay.classList.remove("hidden");
  renderTourStep();
}

function stopWalkthrough() {
  const overlay = document.getElementById("walkthroughOverlay");
  if (overlay) overlay.classList.add("hidden");
  document.querySelectorAll(".tour-highlight").forEach((el) => {
    el.classList.remove("tour-highlight", "tour-blink", "tour-pulse");
  });
}

function renderTourStep() {
  const step = TOUR_STEPS[currentTourIndex];
  if (!step) return;

  // Clear previous highlights and blink animations
  document.querySelectorAll(".tour-highlight, .tour-blink, .tour-pulse").forEach((el) => {
    el.classList.remove("tour-highlight", "tour-blink", "tour-pulse");
  });

  // Switch tab if specified
  if (step.tab) {
    switchTab(step.tab);
  }

  // Update badge and text
  const badge = document.getElementById("tourStepBadge");
  const title = document.getElementById("tourTitle");
  const desc = document.getElementById("tourDescription");
  const prevBtn = document.getElementById("tourPrevBtn");
  const nextBtn = document.getElementById("tourNextBtn");
  const dotsContainer = document.getElementById("tourDots");

  if (badge) badge.innerText = `Step ${currentTourIndex + 1} of ${TOUR_STEPS.length}`;
  if (title) title.innerText = step.title;
  if (desc) desc.innerText = step.description;

  if (dotsContainer) {
    dotsContainer.innerHTML = TOUR_STEPS.map((_, i) => `
      <span class="w-1.5 h-1.5 rounded-full transition-all ${i === currentTourIndex ? 'bg-cyan-400 w-3' : 'bg-dark-600'}"></span>
    `).join("");
  }

  if (prevBtn) prevBtn.style.display = currentTourIndex === 0 ? "none" : "block";
  if (nextBtn) nextBtn.innerText = currentTourIndex === TOUR_STEPS.length - 1 ? "Finish ✓" : "Next →";

  // Mark the target module, trigger a distinct blink once, and scroll into view
  setTimeout(() => {
    const targetEl = document.getElementById(step.targetId);
    if (targetEl) {
      targetEl.classList.add("tour-highlight", "tour-blink");
      targetEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
      
      // Keep persistent highlight after blink completes
      setTimeout(() => {
        targetEl.classList.remove("tour-blink");
      }, 900);
    }
  }, 100);
}

function nextTourStep() {
  if (currentTourIndex < TOUR_STEPS.length - 1) {
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

if "// ==========================================\n// 12. WALKTHROUGH TOUR ENGINE" in js:
    js = js.split("// ==========================================\n// 12. WALKTHROUGH TOUR ENGINE")[0] + walkthrough_section
elif "// ==========================================\n// 8. INTERACTIVE GUIDED WALKTHROUGH" in js:
    js = js.split("// ==========================================\n// 8. INTERACTIVE GUIDED WALKTHROUGH")[0] + walkthrough_section
else:
    js = js + "\n\n" + walkthrough_section

# Write across all static distributions
for folder in ["backend/static", "public", "public/static", "."]:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(folder, "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    with open(os.path.join(folder, "app.js"), "w", encoding="utf-8") as f:
        f.write(js)

print("Successfully removed blur and added single-blink marking for walkthrough!")
