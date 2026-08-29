import os

# 1. Update index.html
with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update Phone number to +91 7667102054
html = html.replace("+91 76671020", "+91 7667102054")

# Update Header Markup to fix wrapping and alignment issues
old_header_start = '<header class="sticky top-0 z-40 bg-dark-800/80 backdrop-blur-md border-b border-dark-600/60 px-6 py-3.5 flex items-center justify-between transition-all">'
old_header_end = '</header>'

new_header = '''  <!-- TOP NAVIGATION HEADER -->
  <header class="sticky top-0 z-40 bg-dark-800/90 backdrop-blur-md border-b border-dark-600/60 px-4 sm:px-6 py-2.5 flex items-center justify-between gap-4 transition-all">
    <div class="flex items-center space-x-3 shrink-0">
      <button id="btnHeaderToggleSidebar" onclick="toggleSidebar()" title="Toggle Sidebar (Ctrl+B)" class="p-2 rounded-lg bg-dark-700 hover:bg-dark-600 border border-dark-600 text-slate-300 hover:text-cyan-400 text-xs transition-all flex items-center justify-center shrink-0">
        <i data-lucide="panel-left" class="w-4 h-4"></i>
      </button>
      
      <!-- Brand & Subtitle (Guaranteed No Wrap & Clean Alignment) -->
      <div class="flex items-center space-x-3 group cursor-pointer shrink-0" onclick="switchTab('explorer')">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-indigo-600 to-emerald-500 p-0.5 shadow-lg shadow-cyan-500/20 group-hover:shadow-cyan-500/40 transition-all duration-300 shrink-0">
          <div class="w-full h-full bg-dark-900 rounded-[10px] flex items-center justify-center">
            <i data-lucide="shield-alert" class="w-5 h-5 text-cyan-400"></i>
          </div>
        </div>
        <div class="shrink-0 flex flex-col justify-center">
          <div class="flex items-center space-x-2 whitespace-nowrap">
            <h1 class="text-base sm:text-lg font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">SENTINEL<span class="text-cyan-400">GRAPH</span></h1>
            <span class="text-[9px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">AML v1.0</span>
          </div>
          <p class="text-[11px] text-slate-400 whitespace-nowrap font-medium leading-none mt-0.5">CognoDB Graph Intelligence Platform</p>
        </div>
      </div>
    </div>

    <!-- Quick Search Input (Cleanly flexed) -->
    <div class="relative hidden lg:block flex-1 max-w-sm mx-4">
      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
        <i data-lucide="search" class="w-4 h-4"></i>
      </div>
      <input 
        type="text" 
        id="globalSearchInput" 
        placeholder="Search entities, accounts, persons..." 
        class="w-full pl-9 pr-4 py-1.5 text-xs rounded-lg bg-dark-700/80 border border-dark-600 text-slate-200 placeholder-slate-400 focus:outline-none focus:border-cyan-500/80 focus:ring-1 focus:ring-cyan-500/80 transition-all"
      >
      <div id="searchResultsDropdown" class="hidden absolute left-0 right-0 top-full mt-1.5 bg-dark-800 border border-dark-600 rounded-lg shadow-2xl z-50 max-h-72 overflow-y-auto divide-y divide-dark-700/60"></div>
    </div>

    <!-- Right Header Tools -->
    <div class="flex items-center space-x-2.5 shrink-0">
      <!-- Candidate Profile / Return to Landing button -->
      <button 
        id="btnShowLanding" 
        onclick="showLandingPage()" 
        title="Back to Landing Page"
        class="hidden sm:flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-dark-700/80 hover:bg-dark-600 border border-dark-600 text-xs text-slate-300 hover:text-cyan-300 transition-all shrink-0"
      >
        <i data-lucide="home" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span class="font-medium whitespace-nowrap">Robin Burdewa</span>
      </button>

      <!-- Database Connection Status Badge -->
      <div id="dbStatusBadge" class="flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-dark-700 border border-dark-600 text-xs text-slate-300 shrink-0">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span id="dbStatusText" class="font-medium whitespace-nowrap">Connecting...</span>
      </div>

      <!-- Walkthrough Tour Button -->
      <button 
        id="btnStartWalkthrough" 
        onclick="startWalkthrough()" 
        title="Start Interactive App Walkthrough"
        class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500/20 via-indigo-500/20 to-emerald-500/20 hover:from-cyan-500/30 hover:to-emerald-500/30 border border-cyan-500/40 text-cyan-300 text-xs font-bold transition-all hover:scale-[1.03] active:scale-[0.98] shadow-lg shadow-cyan-500/10 shrink-0"
      >
        <i data-lucide="compass" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span class="whitespace-nowrap">Walkthrough</span>
      </button>

      <!-- Seed Database Button -->
      <button 
        id="btnSeedDb" 
        onclick="triggerSeed()" 
        title="Seed realistic crime syndicate dataset into CognoDB"
        class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/20 border border-cyan-500/30 text-cyan-400 text-xs font-semibold transition-all hover:scale-[1.02] active:scale-[0.98] shrink-0"
      >
        <i data-lucide="database" class="w-3.5 h-3.5"></i>
        <span class="whitespace-nowrap">Seed CognoDB</span>
      </button>

      <!-- Refresh Graph Button -->
      <button 
        onclick="loadInitialGraph()" 
        title="Reload live graph data"
        class="p-2 rounded-lg bg-dark-700 hover:bg-dark-600 border border-dark-600 text-slate-300 hover:text-white text-xs transition-all shrink-0"
      >
        <i data-lucide="rotate-cw" class="w-4 h-4"></i>
      </button>
    </div>
  </header>'''

# Replace header block
if '<header class="sticky top-0' in html:
    parts = html.split('<header class="sticky top-0')
    rest = parts[1].split('<!-- STATS RIBBON -->')
    html = parts[0] + new_header.strip() + '\n\n  <!-- STATS RIBBON -->' + rest[1]

# 2. Update README.md with correct contact number
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("+91 76671020", "+91 7667102054")
with open("README.md", "w", encoding="utf-8") as f:
    readme = f.write(readme)

# Write index.html across all locations
for folder in ["backend/static", "public", "public/static", "."]:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Alignment fixed and phone number updated to +91 7667102054 across all locations!")
