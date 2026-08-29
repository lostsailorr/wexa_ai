import os

# 1. Update index.html
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace any existing welcomeModal with full Landing Page
landing_page_html = '''
  <!-- ========================================================= -->
  <!-- FULL SCREEN MODERN LANDING PAGE (ROBIN BURDEWA) -->
  <!-- ========================================================= -->
  <div id="landingPage" class="fixed inset-0 z-[100] bg-[#070b14] text-slate-100 flex flex-col justify-between overflow-y-auto selection:bg-cyan-500 selection:text-dark-900 transition-all duration-500">
    
    <!-- Background Ambient Glow Gradients -->
    <div class="fixed inset-0 pointer-events-none overflow-hidden z-0">
      <div class="absolute -top-40 -left-40 w-[600px] h-[600px] bg-cyan-500/10 rounded-full blur-[140px]"></div>
      <div class="absolute top-1/3 -right-40 w-[600px] h-[600px] bg-indigo-600/10 rounded-full blur-[160px]"></div>
      <div class="absolute -bottom-40 left-1/3 w-[600px] h-[600px] bg-emerald-500/10 rounded-full blur-[140px]"></div>
      <div class="absolute inset-0 bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:24px_24px] opacity-25"></div>
    </div>

    <!-- Top Navigation Header for Landing Page -->
    <header class="relative z-10 w-full max-w-7xl mx-auto px-6 py-6 flex items-center justify-between border-b border-dark-700/50">
      <div class="flex items-center space-x-3.5">
        <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-cyan-500 via-indigo-600 to-emerald-500 p-0.5 shadow-xl shadow-cyan-500/25">
          <div class="w-full h-full bg-dark-900 rounded-[14px] flex items-center justify-center">
            <i data-lucide="shield-alert" class="w-6 h-6 text-cyan-400"></i>
          </div>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="text-xl font-black tracking-tight text-white">SENTINEL<span class="text-cyan-400">GRAPH</span></h1>
            <span class="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">AML v1.0</span>
          </div>
          <p class="text-xs text-slate-400 font-medium">CognoDB Real-Time Graph Intelligence Platform</p>
        </div>
      </div>

      <!-- Candidate Contact Badge & CTA -->
      <div class="flex items-center space-x-4">
        <div class="hidden md:flex items-center space-x-3 px-3.5 py-1.5 rounded-xl bg-dark-800/80 border border-dark-700">
          <div class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold text-xs flex items-center justify-center">RB</div>
          <div class="text-left">
            <div class="text-xs font-bold text-slate-200">Robin Burdewa</div>
            <div class="text-[11px] text-cyan-400 font-mono">+91 76671020</div>
          </div>
        </div>

        <button 
          onclick="launchApp()" 
          class="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 via-cyan-400 to-emerald-400 hover:from-cyan-400 hover:to-emerald-300 text-dark-950 text-xs font-extrabold transition-all hover:scale-[1.03] active:scale-[0.98] shadow-lg shadow-cyan-500/25"
        >
          <span>Start App</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </button>
      </div>
    </header>

    <!-- Main Hero Section -->
    <main class="relative z-10 w-full max-w-7xl mx-auto px-6 py-12 lg:py-16 flex flex-col items-center text-center">
      
      <!-- Assignment & Tech Pill -->
      <div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-dark-800/90 border border-cyan-500/30 text-xs font-semibold text-cyan-300 mb-8 shadow-inner">
        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
        <span>CognoDB Assignment 2 Submission for Wexa AI</span>
        <span class="text-slate-500">•</span>
        <span class="text-slate-300">FastAPI & openCypher Cloud</span>
      </div>

      <!-- Hero Heading -->
      <h2 class="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-white max-w-4xl leading-[1.15] mb-6">
        Next-Generation <span class="bg-gradient-to-r from-cyan-400 via-sky-300 to-emerald-400 bg-clip-text text-transparent">Graph Intelligence</span> for Financial Crime Forensics
      </h2>

      <!-- Subtitle -->
      <p class="text-base sm:text-lg text-slate-300 max-w-2xl leading-relaxed mb-10">
        Unmasking complex money laundering rings, multi-tier offshore holding chains, and sanctions evasion corridors at sub-second speeds on <strong>CognoDB Cloud</strong>.
      </p>

      <!-- Primary Action Buttons -->
      <div class="flex flex-col sm:flex-row items-center gap-4 mb-12 w-full sm:w-auto">
        <button 
          onclick="launchApp()" 
          class="w-full sm:w-auto flex items-center justify-center space-x-2.5 px-8 py-4 rounded-2xl bg-gradient-to-r from-cyan-500 via-cyan-400 to-emerald-400 hover:from-cyan-400 hover:to-emerald-300 text-dark-950 text-sm font-extrabold transition-all hover:scale-[1.03] active:scale-[0.98] shadow-2xl shadow-cyan-500/35"
        >
          <i data-lucide="play" class="w-4 h-4 fill-current"></i>
          <span>Launch SentinelGraph App</span>
        </button>

        <button 
          onclick="launchAppWithTour()" 
          class="w-full sm:w-auto flex items-center justify-center space-x-2.5 px-7 py-4 rounded-2xl bg-dark-800 hover:bg-dark-700 border-2 border-cyan-500/40 hover:border-cyan-400 text-cyan-300 hover:text-white text-sm font-bold transition-all hover:scale-[1.03] active:scale-[0.98] shadow-xl shadow-cyan-500/10"
        >
          <i data-lucide="compass" class="w-4 h-4 text-cyan-400"></i>
          <span>Start Guided Walkthrough</span>
        </button>
      </div>

      <!-- First-Time Evaluation Note Banner -->
      <div class="w-full max-w-3xl bg-gradient-to-r from-cyan-950/40 via-dark-800/80 to-indigo-950/40 border border-cyan-500/40 rounded-2xl p-5 mb-16 text-left flex items-start space-x-4 shadow-xl">
        <div class="p-2.5 rounded-xl bg-cyan-500/20 text-cyan-400 shrink-0 mt-0.5">
          <i data-lucide="info" class="w-5 h-5 animate-pulse"></i>
        </div>
        <div class="space-y-1">
          <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wider flex items-center space-x-2">
            <span>First time evaluating this platform?</span>
          </h4>
          <p class="text-xs text-slate-200 leading-relaxed">
            Click <button onclick="launchAppWithTour()" class="text-cyan-300 font-bold underline hover:text-white transition-colors">Start Guided Walkthrough</button> or find the <span class="text-cyan-300 font-semibold">🧭 Walkthrough</span> button in the top navigation bar once inside the app. It provides an interactive 8-step tour highlighting <strong>Smurfing Cycle Rings</strong>, <strong>Recursive UBO Chains</strong>, <strong>Sanctions Path Tracer</strong>, and the <strong>live openCypher Console</strong>.
          </p>
        </div>
      </div>

      <!-- Core Intelligence Capabilities 4-Card Grid -->
      <div class="w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 text-left">
        
        <!-- Card 1: Smurfing -->
        <div class="p-6 rounded-2xl bg-dark-800/60 border border-dark-700/80 hover:border-amber-500/50 hover:bg-dark-800 transition-all duration-300 group">
          <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400 mb-4 group-hover:scale-110 transition-transform">
            <i data-lucide="repeat" class="w-5 h-5"></i>
          </div>
          <h3 class="text-sm font-bold text-white mb-2">Smurfing Rings (Cycles)</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Automated cycle detection traverses layered 3-to-6 hop transaction loops routing money back to the originator.
          </p>
        </div>

        <!-- Card 2: UBO Chains -->
        <div class="p-6 rounded-2xl bg-dark-800/60 border border-dark-700/80 hover:border-cyan-500/50 hover:bg-dark-800 transition-all duration-300 group">
          <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 mb-4 group-hover:scale-110 transition-transform">
            <i data-lucide="git-fork" class="w-5 h-5"></i>
          </div>
          <h3 class="text-sm font-bold text-white mb-2">Recursive 8-Tier UBO</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Unwinds deep offshore holding structures (BVI, Cyprus, Panama) and computes effective ownership percentages.
          </p>
        </div>

        <!-- Card 3: Sanctions -->
        <div class="p-6 rounded-2xl bg-dark-800/60 border border-dark-700/80 hover:border-crimson-500/50 hover:bg-dark-800 transition-all duration-300 group">
          <div class="w-10 h-10 rounded-xl bg-crimson-500/10 border border-crimson-500/20 flex items-center justify-center text-crimson-400 mb-4 group-hover:scale-110 transition-transform">
            <i data-lucide="shield-alert" class="w-5 h-5"></i>
          </div>
          <h3 class="text-sm font-bold text-white mb-2">Sanctions Path Tracer</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Calculates shortest network paths connecting high-risk suspects to OFAC SDN and designated watchlists.
          </p>
        </div>

        <!-- Card 4: openCypher Console -->
        <div class="p-6 rounded-2xl bg-dark-800/60 border border-dark-700/80 hover:border-purple-500/50 hover:bg-dark-800 transition-all duration-300 group">
          <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400 mb-4 group-hover:scale-110 transition-transform">
            <i data-lucide="terminal" class="w-5 h-5"></i>
          </div>
          <h3 class="text-sm font-bold text-white mb-2">Live openCypher Console</h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            Interactive playground executing native Cypher graph queries directly against CognoDB Cloud with sub-second execution.
          </p>
        </div>

      </div>
    </main>

    <!-- Landing Page Footer -->
    <footer class="relative z-10 w-full max-w-7xl mx-auto px-6 py-6 border-t border-dark-700/50 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-400 gap-3">
      <div class="flex items-center space-x-2">
        <span>Developed by <strong class="text-white">Robin Burdewa</strong></span>
        <span>•</span>
        <span class="font-mono text-cyan-400">+91 76671020</span>
      </div>
      <div>
        <span>Built for <strong>CognoDB Take-Home Assignment 2 (Wexa AI)</strong></span>
      </div>
    </footer>

  </div>
'''

# Remove any old welcomeModal
if '<div id="welcomeModal"' in html:
    parts = html.split('<div id="welcomeModal"')
    rest = parts[1].split('<!-- GUIDED WALKTHROUGH DOCK')
    html = parts[0] + '<!-- GUIDED WALKTHROUGH DOCK' + rest[1]

# Remove any old landingPage if exists
if '<div id="landingPage"' in html:
    parts = html.split('<div id="landingPage"')
    rest = parts[1].split('<!-- GUIDED WALKTHROUGH DOCK')
    html = parts[0] + '<!-- GUIDED WALKTHROUGH DOCK' + rest[1]

# Insert Landing Page before walkthrough dock
html = html.replace('<!-- GUIDED WALKTHROUGH DOCK', landing_page_html + '\n  <!-- GUIDED WALKTHROUGH DOCK')

# Update header with Landing Page return button
if 'id="btnShowLanding"' not in html:
    html = html.replace(
        '<button \n        id="btnShowWelcome" \n        onclick="openWelcomeModal()" \n        title="Candidate Profile & Overview"\n        class="hidden sm:flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg bg-dark-700/80 hover:bg-dark-600 border border-dark-600 text-xs text-slate-300 hover:text-cyan-300 transition-all"\n      >\n        <i data-lucide="user-check" class="w-3.5 h-3.5 text-cyan-400"></i>\n        <span class="font-medium">Robin Burdewa</span>\n      </button>',
        '<button \n        id="btnShowLanding" \n        onclick="showLandingPage()" \n        title="Back to Landing Page"\n        class="hidden sm:flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg bg-dark-700/80 hover:bg-dark-600 border border-dark-600 text-xs text-slate-300 hover:text-cyan-300 transition-all"\n      >\n        <i data-lucide="home" class="w-3.5 h-3.5 text-cyan-400"></i>\n        <span class="font-medium">Robin Burdewa</span>\n      </button>'
    )

# 2. Update app.js with landing page controllers
with open("backend/static/app.js", "r", encoding="utf-8") as f:
    js = f.read()

landing_js = '''
// ==========================================
// FULL LANDING PAGE CONTROLLER (ROBIN BURDEWA)
// ==========================================
function launchApp() {
  const landing = document.getElementById("landingPage");
  if (landing) {
    landing.classList.add("opacity-0", "pointer-events-none");
    setTimeout(() => {
      landing.classList.add("hidden");
      if (networkInstance) {
        networkInstance.redraw();
        networkInstance.fit();
      }
    }, 400);
  }
}

function launchAppWithTour() {
  launchApp();
  setTimeout(() => {
    startWalkthrough();
  }, 450);
}

function showLandingPage() {
  const landing = document.getElementById("landingPage");
  if (landing) {
    landing.classList.remove("hidden");
    setTimeout(() => {
      landing.classList.remove("opacity-0", "pointer-events-none");
      if (window.lucide) lucide.createIcons();
    }, 20);
  }
}
'''

if "function openWelcomeModal()" in js:
    js = js.split("// WELCOME MODAL CONTROLLERS")[0] + landing_js
elif "function launchApp()" not in js:
    js = js + "\n" + landing_js

# Write across all static distributions
for folder in ["backend/static", "public", "public/static", "."]:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(folder, "app.js"), "w", encoding="utf-8") as f:
        f.write(js)

print("Full-screen Landing Page successfully created and synchronized across all locations!")
