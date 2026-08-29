import os

# 1. Update index.html
with open("backend/static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add sidebar toggle button in header next to logo
if 'id="btnHeaderToggleSidebar"' not in html:
    html = html.replace(
        '<header class="sticky top-0 z-40 bg-dark-800/80 backdrop-blur-md border-b border-dark-600/60 px-6 py-3.5 flex items-center justify-between transition-all">\n    <div class="flex items-center space-x-4">',
        '<header class="sticky top-0 z-40 bg-dark-800/80 backdrop-blur-md border-b border-dark-600/60 px-6 py-3.5 flex items-center justify-between transition-all">\n    <div class="flex items-center space-x-4">\n      <button id="btnHeaderToggleSidebar" onclick="toggleSidebar()" title="Toggle Sidebar (Ctrl+B)" class="p-2 rounded-lg bg-dark-700 hover:bg-dark-600 border border-dark-600 text-slate-300 hover:text-cyan-400 text-xs transition-all flex items-center justify-center">\n        <i data-lucide="panel-left" class="w-4 h-4"></i>\n      </button>'
    )

# Update sidebar markup with ID, toggle button, and data-tooltips
old_sidebar = '''    <!-- LEFT SIDEBAR: INTELLIGENCE MODULES -->
    <aside class="w-64 bg-dark-800/60 border-r border-dark-700/60 flex flex-col justify-between p-4 shrink-0 overflow-y-auto">
      <div class="space-y-6">
        <div>
          <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2 px-2">Intelligence Modules</div>
          <nav class="space-y-1">
            <button id="tab-explorer" onclick="switchTab('explorer')" class="tab-btn active w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="globe" class="w-4 h-4"></i>
              <span>Graph Explorer</span>
            </button>
            <button id="tab-rings" onclick="switchTab('rings')" class="tab-btn w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <div class="flex items-center space-x-2.5">
                <i data-lucide="repeat" class="w-4 h-4 text-amber-400"></i>
                <span>Smurfing Rings (Cycles)</span>
              </div>
              <span class="px-1.5 py-0.5 text-[10px] font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">2</span>
            </button>
            <button id="tab-ubo" onclick="switchTab('ubo')" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="git-fork" class="w-4 h-4 text-cyan-400"></i>
              <span>UBO Multi-Tier Chains</span>
            </button>
            <button id="tab-sanctions" onclick="switchTab('sanctions')" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="shield-alert" class="w-4 h-4 text-crimson-400"></i>
              <span>Sanctions Path Tracer</span>
            </button>
            <button id="tab-mules" onclick="switchTab('mules')" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="activity" class="w-4 h-4 text-purple-400"></i>
              <span>Mule Transit Hubs</span>
            </button>
            <button id="tab-cypher" onclick="switchTab('cypher')" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="terminal" class="w-4 h-4 text-cyan-400"></i>
              <span>Cypher Playground</span>
            </button>
          </nav>
        </div>'''

new_sidebar = '''    <!-- LEFT SIDEBAR: INTELLIGENCE MODULES & COLLAPSIBLE DRAWER -->
    <aside id="leftSidebar" class="w-64 bg-dark-800/80 border-r border-dark-700/60 flex flex-col justify-between p-4 shrink-0 overflow-y-auto overflow-x-hidden transition-all duration-300 relative group">
      <div class="space-y-6">
        <div>
          <div class="flex items-center justify-between mb-2 px-2">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 sidebar-text">Intelligence Modules</div>
            <button 
              id="btnCollapseSidebar" 
              onclick="toggleSidebar()" 
              title="Collapse / Expand Sidebar (Ctrl+B)" 
              class="p-1 rounded-lg text-slate-400 hover:text-cyan-300 hover:bg-dark-700 transition-colors"
            >
              <i data-lucide="panel-left-close" class="w-4 h-4 sidebar-collapse-icon"></i>
            </button>
          </div>
          <nav class="space-y-1">
            <button id="tab-explorer" onclick="switchTab('explorer')" data-tooltip="Graph Explorer" class="tab-btn active w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="globe" class="w-4 h-4 shrink-0"></i>
              <span class="sidebar-text truncate">Graph Explorer</span>
            </button>
            <button id="tab-rings" onclick="switchTab('rings')" data-tooltip="Smurfing Rings (Cycles)" class="tab-btn w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <div class="flex items-center space-x-2.5 truncate">
                <i data-lucide="repeat" class="w-4 h-4 text-amber-400 shrink-0"></i>
                <span class="sidebar-text truncate">Smurfing Rings (Cycles)</span>
              </div>
              <span class="sidebar-text px-1.5 py-0.5 text-[10px] font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0">2</span>
            </button>
            <button id="tab-ubo" onclick="switchTab('ubo')" data-tooltip="UBO Multi-Tier Chains" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="git-fork" class="w-4 h-4 text-cyan-400 shrink-0"></i>
              <span class="sidebar-text truncate">UBO Multi-Tier Chains</span>
            </button>
            <button id="tab-sanctions" onclick="switchTab('sanctions')" data-tooltip="Sanctions Path Tracer" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="shield-alert" class="w-4 h-4 text-crimson-400 shrink-0"></i>
              <span class="sidebar-text truncate">Sanctions Path Tracer</span>
            </button>
            <button id="tab-mules" onclick="switchTab('mules')" data-tooltip="Mule Transit Hubs" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="activity" class="w-4 h-4 text-purple-400 shrink-0"></i>
              <span class="sidebar-text truncate">Mule Transit Hubs</span>
            </button>
            <button id="tab-cypher" onclick="switchTab('cypher')" data-tooltip="Cypher Playground" class="tab-btn w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-dark-700/60 transition-all text-left">
              <i data-lucide="terminal" class="w-4 h-4 text-cyan-400 shrink-0"></i>
              <span class="sidebar-text truncate">Cypher Playground</span>
            </button>
          </nav>
        </div>'''

if old_sidebar in html:
    html = html.replace(old_sidebar, new_sidebar)

# 2. Update style.css with collapsible sidebar rules and tooltips
with open("backend/static/style.css", "r", encoding="utf-8") as f:
    css = f.read()

if "/* Collapsible Sidebar Drawer */" in css:
    css = css.split("/* Collapsible Sidebar Drawer */")[0]

sidebar_css = '''/* Collapsible Sidebar Drawer & Icon Rail Styles */
#leftSidebar {
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1), padding 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

#leftSidebar.collapsed {
  width: 4.5rem !important; /* 72px icon rail */
  padding-left: 0.6rem !important;
  padding-right: 0.6rem !important;
}

#leftSidebar.collapsed .sidebar-text,
#leftSidebar.collapsed #view-controls {
  display: none !important;
}

#leftSidebar.collapsed .tab-btn {
  justify-content: center !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  position: relative;
}

#leftSidebar.collapsed .tab-btn i {
  margin: 0 auto;
}

/* Floating Tooltips in Collapsed Mode */
#leftSidebar.collapsed .tab-btn:hover::after {
  content: attr(data-tooltip);
  position: absolute;
  left: calc(100% + 12px);
  top: 50%;
  transform: translateY(-50%);
  background-color: #0b1324;
  color: #e2e8f0;
  border: 1px solid rgba(6, 182, 212, 0.5);
  padding: 6px 12px;
  font-size: 11px;
  font-weight: 700;
  border-radius: 8px;
  white-space: nowrap;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.9), 0 0 15px rgba(6, 182, 212, 0.3);
  z-index: 90;
  pointer-events: none;
}
'''

css = css.strip() + "\n\n" + sidebar_css

# 3. Update app.js with toggleSidebar function
with open("backend/static/app.js", "r", encoding="utf-8") as f:
    js = f.read()

sidebar_js = '''
// ==========================================
// COLLAPSIBLE SIDEBAR CONTROLLER
// ==========================================
function toggleSidebar() {
  const sidebar = document.getElementById("leftSidebar");
  const collapseIcon = document.querySelector(".sidebar-collapse-icon");
  if (!sidebar) return;

  const isCollapsed = sidebar.classList.toggle("collapsed");
  
  if (collapseIcon) {
    collapseIcon.setAttribute("data-lucide", isCollapsed ? "panel-left-open" : "panel-left-close");
    if (window.lucide) lucide.createIcons();
  }

  // Smoothly trigger vis.js resize / redraw
  setTimeout(() => {
    if (networkInstance) {
      networkInstance.redraw();
      networkInstance.fit();
    }
  }, 320);
}

// Global keyboard shortcut Ctrl+B or Cmd+B to toggle sidebar
document.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "b") {
    e.preventDefault();
    toggleSidebar();
  }
});
'''

if "function toggleSidebar()" not in js:
    js = js + "\n" + sidebar_js

# Write across all static distributions
for folder in ["backend/static", "public", "public/static", "."]:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(folder, "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    with open(os.path.join(folder, "app.js"), "w", encoding="utf-8") as f:
        f.write(js)

print("Collapsible sidebar drawer successfully created and synchronized across all locations!")
