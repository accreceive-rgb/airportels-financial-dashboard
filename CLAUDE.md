# Airportels Financial — MADGA Project Rules

> This file tells Claude how to work on this MADGA project.
> It is auto-generated during project setup. Do not delete.

---

## On Session Start (Every Time)

1. `git pull origin main --rebase` (silent unless there's news)
   - If conflict: auto-resolve (see Conflict Resolution below)
   - If fail (no internet): continue offline (see Offline Handling below)
2. Read all existing `.md` files to understand current state
3. Read `changelog.md` to see what changed since last session
4. Note what's still marked TBD or stub
5. If others made changes, briefly tell the user what's new
6. Ask the user: "What would you like to work on?"

**The user may want to:**
- Fill in TBD gaps
- Add a new process
- Update existing details
- Create or update a plan
- Discuss improvements (auto-create a plan)

---

## Quick Commands

Recognize these phrases and act immediately:

| Command | What to do |
|---|---|
| **"add process"** / **"new process"** | Ask for process name, then collect info |
| **"update [process name]"** | Open that process's files, ask what to change |
| **"show TBDs"** / **"what's missing"** | Scan all `.md` files, list every TBD field grouped by process |
| **"rebuild dashboard"** | Re-read all `.md` files, regenerate full `DASHBOARD_DATA` + HTML |
| **"new plan for [process]"** | Create a plan file linked to that process |
| **"show status"** | Summary: total processes by completeness, active plans, recent changes |
| **"what's next"** | Read changelog.md, find latest suggested next steps and TBD list |
| **"add team member"** | Add person to `department/overview.md` + update dashboard |
| **"change [process] to [status]"** | Update status, run lifecycle rules + impact check |
| **"show flow for [process]"** | Generate/display the Mermaid flowchart for that process |
| **"sync"** / **"pull latest"** | `git pull origin main --rebase`, report what changed |
| **"who changed what"** | Show recent `git log --oneline -10` in plain language |
| **"save"** / **"push"** | Commit all current changes and push to remote |
| **"update project link"** | Read new `.setup` file, update git remote URL |
| **"export data"** / **"update data.json"** | Regenerate `dashboard/data.json` from all `.md` files |

Also recognize natural variations — "anything incomplete", "what do we still need" → same as "show TBDs".

---

## Git Auto-Sync Protocol

Claude handles all git operations automatically. **Never ask the user about git.**

### After every meaningful change:

```
1. git add -A
2. git commit -m "<what changed> — by <user.name>"
3. git push origin main
   - If push fails (someone pushed): pull --rebase, then push again
   - If push fails (no internet): commit locally, queue for next sync
```

**Meaningful change =** any `.md` file created/updated, dashboard HTML updated, plan created/modified.
**Not meaningful =** mid-edit saves or partial work (wait until complete).

### On session end:

```
1. Write changelog.md entry
2. git add -A
3. git commit -m "Session end: <summary> — by <user.name>"
4. git push origin main
5. Confirm to user:
   - Online: "All changes saved and synced with the team."
   - Offline: "Changes saved locally. They'll sync next time you're online."
```

### Offline Handling

When git push/pull fails (no internet):
- **Never block work.** Continue normally — changes are committed locally.
- Tell the user **once**: "You're offline. I'm saving everything locally. It'll sync when you're back online."
- Don't repeat the warning in the same session.
- On next session, retry push. If it works: "You're back online — synced all changes."

### Conflict Resolution

When `git pull --rebase` hits a conflict:
1. **`.md` files:** Accept BOTH versions — merge content. If fields conflict, keep remote version + note in changelog.
2. **`dashboard/index.html`:** Always regenerate from `.md` files after resolving.
3. **`changelog.md`:** Keep both entries.
4. Commit and push the merge.
5. Tell the user briefly what happened.

**Never ask the user to resolve git conflicts.**

### Security

- Never show `REPO_URL` contents (contains token) — always mask: `https://***@github.com/org/repo.git`
- Never commit `.setup` files
- If user asks about setup: "That's your connection config — already used during setup."

---

## Dashboard Sync Rule (CRITICAL)

**Every time a `.md` file is created, updated, or deleted, immediately sync the dashboard:**

1. Update `DASHBOARD_DATA` in `dashboard/index.html`
2. New process → add to `process-map.md` AND `DASHBOARD_DATA.processes` (include empty `diagrams: []`) AND generate sub-page at `dashboard/pages/process-<slug>.html`
3. Updated process → update `DASHBOARD_DATA` AND regenerate the process sub-page
4. New/updated plan → add/update in `DASHBOARD_DATA.plans` (auto-generate `gantt` if 3+ dated actions)
5. New/updated diagram → add to `DASHBOARD_DATA.processes[].diagrams[]` AND update the process sub-page
6. Update `updatedAt` timestamp and ensure `version` matches `.madga`
7. Add an entry to `DASHBOARD_DATA.activity` describing the change (user, action, target, detail, type)
8. Export `dashboard/data.json` — full mirror of ALL `.md` content as structured JSON

**Never leave the dashboard out of sync.** `.md` files = source of truth, `index.html` = overview, sub-pages = full detail view, `data.json` = full export for central dashboard.

---

## Central Dashboard Data Export (data.json)

Every time the dashboard syncs, also write `dashboard/data.json`. This file feeds the central dashboard.

`data.json` captures EVERYTHING — full text from overview.md, full step details, full plan analysis, full cross-links with department slugs.

**Generation rule:** Run AFTER updating `DASHBOARD_DATA` in `index.html`. Read all `.md` files and build the complete JSON. Must be valid JSON (no template literals, no JS — pure JSON).

The `department` field in cross-links enables cross-department flow diagrams. Use the department slug from `.madga`.

**The file is committed to git** — it triggers the webhook pipeline to the central dashboard.

---

## Cross-Process Impact Check

**When updating or changing a process, check for ripple effects:**

1. Read the process's `Cross-Department Links` (receives from / hands off to)
2. Search other processes for references to the changed process
3. If linked processes exist, warn the user:
   > "This process hands off to **[Process B]** and receives from **[Process C]**. Your changes might affect them. Want me to check?"
4. If confirmed, review linked processes and flag what may need updating
5. Log the impact check in changelog

**Applies to:** changing steps, inputs/outputs, tools, or setting status to `inactive`.

---

## Process Status Lifecycle

```
active ──> under-review ──> active (updated)
                        ──> inactive
inactive ──> active (reactivated)
```

**When moving to `under-review`:**
- Yellow indicator on dashboard
- Check if a plan exists — if not, prompt to create one
- Note in changelog.md

**When moving to `inactive`:**
- Run cross-process impact check
- Gray styling on dashboard
- Check plans referencing this process → set to `on-hold`
- Note in changelog.md

**When moving back to `active`:**
- Remove inactive styling
- Check if plans were put `on-hold` → prompt to reactivate
- Note in changelog.md

**Always update together:** process overview.md `status` → `process-map.md` → `DASHBOARD_DATA` → changelog.md.

---

## Handling Missing Information (CRITICAL)

- **Never block progress.** If info is missing, use `TBD` and move on.
- **Never say "I need X before I can continue."** You can ALWAYS continue.
- **Mark completeness honestly** — `full` / `partial` / `stub` in frontmatter
- **Track TBDs** — at session end, summarize what's filled vs TBD
- **Partial is fine** — 3 of 10 fields filled is still valuable
- **Stub entries welcome** — process name with zero details? Create a stub file anyway

---

## Handling User Files & Media

- **Screenshots/images** — extract all visible text, labels, connections, flows. Organize into `.md` structure.
- **PDFs/docs** — read and extract. If hard to parse, ask for screenshot of key parts.
- **Links** — if can't access, ask for screenshot.
- **Messy diagrams** — do your best, show user what you extracted, confirm before committing.

---

## Flowcharts & Diagrams — Mermaid.js ONLY (STRICT)

> **ALL flowcharts, process flows, diagrams MUST use Mermaid.js. No exceptions.**
>
> **NEVER** hand-code flowcharts with CSS, SVG, HTML divs, flexbox, canvas, or any other method.
> If it looks like a flow or diagram → deferred Mermaid pattern. Period.

### Deferred Mermaid Rendering (CRITICAL):

**Never use `startOnLoad: true`** — diagrams in hidden tabs/collapsed cards render with zero dimensions.

```html
<!-- CORRECT — deferred rendering -->
<div class="mermaid-pending" data-mermaid-src="graph LR A-->B"></div>
```

Call `renderVisibleMermaid()` after: tab switch, card expand, filter change, page load.

### Diagram Types:
- **Flowchart** — `graph LR/TD` — process steps, decisions. Max 12 nodes, 2 decision branches.
- **Swimlane** — `graph` + `subgraph` — multi-actor processes. Max 4 lanes, 10 nodes.
- **Sequence** — `sequenceDiagram` — system interactions, back-and-forth. Max 6 participants, 15 messages.
- **Gantt** — `gantt` — plan timelines. Auto-generate when plan has 3+ dated actions.
- **State** — `stateDiagram-v2` — status lifecycles, approval flows. Max 8 states.

### Node shapes:
- `([text])` — start/end
- `[text]` — normal step
- `{text}` — decision
- `[[text]]` — subprocess

---

## File Templates Reference

### Process overview (`processes/<slug>/overview.md`)
Frontmatter: `title`, `process_id`, `owner`, `category`, `status`, `completeness`, `updated`
Sections: Purpose, Stakeholders table, Tools & Systems table, Timing, Inputs, Outputs, Cross-Department Links, Pain Points

### Process steps (`processes/<slug>/steps.md`)
Frontmatter: `title`, `process_id`, `updated`
Content: Steps table (# / Step / Actor / Tool / Output / Notes) + Step Details subsections

### Plans (`plans/<slug>.md`)
Frontmatter: `title`, `related_process`, `status`, `owner`, `created`, `updated`
Sections: Problem, Analysis, Plan (Actions table + Dependencies + Risks + Success Criteria)

### Process map (`department/process-map.md`)
Master index table: # / Process (linked) / Owner / Category / Status / Completeness

---

## When User Discusses Improvements

Automatically create/update a plan file in `plans/`:
- Use Problem > Analysis > Plan structure
- Link to the relevant process
- Update dashboard to reflect the new plan

---

## Session End — Changelog Entry (REQUIRED)

Before closing, **always** write to `changelog.md` (newest entry at top):

```markdown
## <YYYY-MM-DD> — Session summary

### What was done
- <bullet list>

### Files changed
- `path/to/file.md` — what changed

### Still TBD
- <list of incomplete items>

### Suggested next steps
- <what to work on next session>

---
```

---

## File Conventions

- **File naming:** lowercase, hyphens for spaces (e.g., `order-fulfillment`)
- **YAML frontmatter:** every `.md` file must have YAML frontmatter with at least `title` and `updated` fields
- **`detail/` subfolder:** only create inside a process folder when a step is complex enough for its own file
- **HTML `<title>`:** `Airportels Financial — MADGA` for `index.html`, `<Process Name> — Airportels Financial MADGA` for sub-pages
- **MADGA badge:** `<span class="text-xs font-mono bg-gray-800 text-white px-2 py-1 rounded">MADGA</span>`

---

## Dashboard Structure

- **`dashboard/index.html`** — main dashboard: 5 tabs (Overview, Processes, Plans, Diagrams, Activity)
- **`dashboard/pages/process-<slug>.html`** — one per process, full detail page
- **`dashboard/data.json`** — full JSON export for central dashboard

### Process Sub-Pages — Generated when process is created, updated when process changes:
1. Back to Dashboard link
2. Header — name, status badge, category badge, purpose, owner, completeness
3. Two-column — timing/inputs/outputs + tools/cross-department links
4. Stakeholders table
5. Step-by-step breakdown table
6. Process Diagrams — ALL diagrams inline (deferred Mermaid)
7. Pain Points — red-dotted list
8. Related Improvement Plans — linked plan cards
9. Footer — dynamic version

---

## Build Rules

- No npm, no build tools, no frameworks (beyond Tailwind, Mermaid, Chart.js via CDN)
- Dashboard works by double-click — no server needed
- Split HTML to sub-pages when content grows (>600 lines or >8 steps)
- Keep `.md` files under ~150 lines — split if larger
- `process-map.md` is always the master index
- Plans are separate from process docs
