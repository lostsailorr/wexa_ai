import os

# 1. Update index.html
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Welcome / Start Screen Modal
welcome_modal = '''
  <!-- ========================================================= -->
  <!-- START / WELCOME MODAL OVERLAY (ROBIN BURDEWA) -->
  <!-- ========================================================= -->
  <div id="welcomeModal" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-dark-950/85 backdrop-blur-sm transition-all duration-300">
    <div class="relative w-full max-w-2xl bg-dark-800/98 border-2 border-cyan-500/80 rounded-3xl p-6 sm:p-8 shadow-2xl shadow-cyan-500/25 overflow-hidden animate-fadeIn">
      
      <!-- Top Decorative Glow -->
      <div class="absolute -top-24 -left-24 w-48 h-48 bg-cyan-500/20 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -top-24 -right-24 w-48 h-48 bg-indigo-500/20 rounded-full blur-3xl pointer-events-none"></div>

      <!-- Header & Platform Badge -->
      <div class="flex items-center justify-between border-b border-dark-700/80 pb-5 mb-6">
        <div class="flex items-center space-x-3.5">
          <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-cyan-500 via-indigo-600 to-emerald-500 p-0.5 shadow-lg shadow-cyan-500/30">
            <div class="w-full h-full bg-dark-900 rounded-[14px] flex items-center justify-center">
              <i data-lucide="shield-alert" class="w-6 h-6 text-cyan-400"></i>
            </div>
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h2 class="text-xl font-extrabold tracking-tight text-white">SENTINEL<span class="text-cyan-400">GRAPH</span></h2>
              <span class="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">AML v1.0</span>
            </div>
            <p class="text-xs text-slate-400 font-medium">CognoDB Real-Time Graph Intelligence Platform</p>
          </div>
        </div>

        <button onclick="dismissWelcomeModal()" class="p-1.5 rounded-xl text-slate-400 hover:text-white hover:bg-dark-700/80 transition-colors">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Candidate & Developer Info Card -->
      <div class="bg-gradient-to-r from-cyan-950/40 via-dark-700/50 to-indigo-950/40 border border-cyan-500/30 rounded-2xl p-4 mb-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-full bg-cyan-500/20 border border-cyan-400/40 flex items-center justify-center text-cyan-300 font-bold text-sm">
            RB
          </div>
          <div>
            <div class="text-sm font-bold text-white flex items-center space-x-2">
              <span>Robin Burdewa</span>
              <span class="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Developer / Candidate</span>
            </div>
            <div class="text-xs text-slate-300 flex items-center space-x-1.5 mt-0.5">
              <i data-lucide="phone" class="w-3.5 h-3.5 text-cyan-400"></i>
              <span class="font-mono text-cyan-200">+91 76671020</span>
            </div>
          </div>
        </div>

        <div class="text-right sm:text-right w-full sm:w-auto">
          <span class="text-[11px] text-slate-400 uppercase tracking-wider font-semibold">CognoDB Assignment 2</span>
        </div>
      </div>

      <!-- First Time User Note Alert -->
      <div class="bg-cyan-500/10 border border-cyan-500/30 rounded-2xl p-4 mb-6 flex items-start space-x-3.5">
        <div class="p-2 rounded-xl bg-cyan-500/20 text-cyan-400 shrink-0 mt-0.5">
          <i data-lucide="compass" class="w-5 h-5 animate-pulse"></i>
        </div>
        <div class="space-y-1">
          <h4 class="text-xs font-bold text-cyan-300 uppercase tracking-wide flex items-center space-x-1.5">
            <span>First time here?</span>
          </h4>
          <p class="text-xs text-slate-200 leading-relaxed">
            Check out our <span class="text-cyan-300 font-semibold underline underline-offset-2">🧭 Walkthrough</span> button in the top navigation bar! It guides you step-by-step through our <strong>Smurfing Cycle Rings</strong>, <strong>Recursive UBO Chains</strong>, <strong>Sanctions Tracer</strong>, and <strong>live openCypher Query Console</strong>.
          </p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row items-center justify-end gap-3 pt-2">
        <button 
          onclick="startWalkthroughFromWelcome()" 
          class="w-full sm:w-auto flex items-center justify-center space-x-2 px-5 py-2.5 rounded-xl bg-dark-700 hover:bg-dark-600 border border-cyan-500/40 text-cyan-300 hover:text-white text-xs font-bold transition-all hover:scale-[1.02] active:scale-[0.98] shadow-lg shadow-cyan-500/10"
        >
          <i data-lucide="compass" class="w-4 h-4 text-cyan-400"></i>
          <span>Start Interactive Walkthrough</span>
        </button>

        <button 
          onclick="dismissWelcomeModal()" 
          class="w-full sm:w-auto flex items-center justify-center space-x-2 px-6 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 via-cyan-400 to-emerald-400 hover:from-cyan-400 hover:to-emerald-300 text-dark-950 text-xs font-extrabold transition-all hover:scale-[1.02] active:scale-[0.98] shadow-xl shadow-cyan-500/25"
        >
          <span>Start Exploring Platform →</span>
        </button>
      </div>

    </div>
  </div>
'''

# Remove any old welcomeModal
if '<div id="welcomeModal"' in html:
    parts = html.split('<div id="welcomeModal"')
    rest = parts[1].split('<!-- ========================================================= -->\n  <!-- GUIDED WALKTHROUGH DOCK')
    if len(rest) > 1:
        html = parts[0] + '  <!-- GUIDED WALKTHROUGH DOCK' + rest[1]
    else:
        rest = parts[1].split('<div id="walkthroughOverlay"')
        html = parts[0] + '<div id="walkthroughOverlay"' + rest[1]

# Insert welcome modal before walkthrough overlay
html = html.replace('<!-- GUIDED WALKTHROUGH DOCK', welcome_modal + '\n  <!-- GUIDED WALKTHROUGH DOCK')

# Add About/Author info button in header before dbStatusBadge
author_btn = '''      <!-- Candidate Info / Start Page Button -->
      <button 
        id="btnShowWelcome" 
        onclick="openWelcomeModal()" 
        title="Candidate Profile & Overview"
        class="hidden sm:flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg bg-dark-700/80 hover:bg-dark-600 border border-dark-600 text-xs text-slate-300 hover:text-cyan-300 transition-all"
      >
        <i data-lucide="user-check" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span class="font-medium">Robin Burdewa</span>
      </button>

'''

if 'id="btnShowWelcome"' not in html:
    html = html.replace('<!-- Database Connection Status Badge -->', author_btn + '      <!-- Database Connection Status Badge -->')

# 2. Update app.js to include welcome modal handlers
with open("backend/static/app.js", "r", encoding="utf-8") as f:
    js = f.read()

welcome_js = '''
// ==========================================
// WELCOME MODAL CONTROLLERS (ROBIN BURDEWA)
// ==========================================
function openWelcomeModal() {
  const modal = document.getElementById("welcomeModal");
  if (modal) modal.classList.remove("hidden");
}

function dismissWelcomeModal() {
  const modal = document.getElementById("welcomeModal");
  if (modal) modal.classList.add("hidden");
}

function startWalkthroughFromWelcome() {
  dismissWelcomeModal();
  setTimeout(() => {
    startWalkthrough();
  }, 150);
}
'''

if "function openWelcomeModal()" not in js:
    js = js + "\n" + welcome_js

# Write across all static distributions
for folder in ["backend/static", "public", "public/static", "."]:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(folder, "app.js"), "w", encoding="utf-8") as f:
        f.write(js)

print("Start page / Welcome modal with Robin Burdewa & Contact info created successfully across all folders!")
