import json
import os


def get_confidence_class(conf):
    if conf >= 0.8:
        return "high"
    elif conf >= 0.5:
        return "medium"
    else:
        return "low"


def generate_html(groups):
    html = """
<!DOCTYPE html>
<html>
<head>
<title>Research Digest</title>

<style>
body {
    font-family: 'Segoe UI', Arial, sans-serif;
    margin: 0;
    padding: 0;
    transition: 0.3s;
}

/* 🌙 DARK MODE */
body.dark {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: #e2e8f0;
}

/* ☀️ LIGHT MODE */
body.light {
    background: #f8fafc;
    color: #0f172a;
}

/* CONTAINER */
.container {
    max-width: 1000px;
    margin: auto;
    padding: 30px 20px;
}

/* HEADER */
h1 {
    font-size: 34px;
    margin-bottom: 25px;
}

/* TOP BAR */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
}

input {
    padding: 10px 14px;
    border-radius: 10px;
    border: none;
    width: 260px;
}

select {
    padding: 10px;
    border-radius: 10px;
    border: none;
    margin-left: 10px;
}

button {
    padding: 10px 14px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    background: linear-gradient(135deg, #6366f1, #4f46e5);
    color: white;
}

/* MODE BASED INPUT */
body.dark input,
body.dark select {
    background: #1e293b;
    color: white;
}

body.light input,
body.light select {
    background: white;
    color: black;
    border: 1px solid #ccc;
}

/* THEME BLOCK */
.theme-block {
    margin-bottom: 40px;
}

/* THEME HEADER */
.theme-header {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
}

/* CARD */
.card {
    padding: 20px;
    margin: 14px 0;
    border-radius: 12px;
    transition: 0.25s;
}

body.dark .card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
}

body.light .card {
    background: white;
    border: 1px solid #e2e8f0;
}

.card:hover {
    transform: translateY(-4px);
}

/* TEXT */
.claim {
    font-weight: 600;
    margin-bottom: 8px;
}

.evidence {
    font-size: 14px;
    margin-bottom: 6px;
}

body.dark .evidence {
    color: #94a3b8;
}

body.light .evidence {
    color: #555;
}

/* CONFIDENCE COLORS */
.high { color: #22c55e; }
.medium { color: #f59e0b; }
.low { color: #ef4444; }

</style>

<script>
function toggleDark() {
    let body = document.body;

    if (body.classList.contains("dark")) {
        body.classList.remove("dark");
        body.classList.add("light");
    } else {
        body.classList.remove("light");
        body.classList.add("dark");
    }
}

function searchClaims() {
    let input = document.getElementById("search").value.toLowerCase();
    let cards = document.getElementsByClassName("card");

    for (let c of cards) {
        let text = c.innerText.toLowerCase();
        c.style.display = text.includes(input) ? "block" : "none";
    }
}

function filterThemes() {
    let value = document.getElementById("themeFilter").value;
    let themes = document.getElementsByClassName("theme-block");

    for (let t of themes) {
        if (value === "all") {
            t.style.display = "block";
        } else {
            t.style.display = t.dataset.theme === value ? "block" : "none";
        }
    }
}
</script>
</head>

<body class="dark">

<div class="container">

<h1>📊 Research Digest</h1>

<div class="top-bar">
    <div>
        <input id="search" onkeyup="searchClaims()" placeholder="🔍 Search claims...">
        <select id="themeFilter" onchange="filterThemes()">
            <option value="all">All Themes</option>
"""

    # Dropdown
    for i in range(len(groups)):
        html += f'<option value="{i}">Theme {i+1}</option>'

    html += """
        </select>
    </div>

    <button onclick="toggleDark()">🌙 Toggle Mode</button>
</div>
"""

    # Themes
    for i, group in enumerate(groups):
        if not group:
            continue

        html += f'<div class="theme-block" data-theme="{i}">'

        html += f"""
<div class="theme-header">
<b>Theme {i+1}</b><br>
{group[0]['claim'][:120]}...<br>
Supporting Claims: {len(group)}
</div>
"""

        for item in group:
            conf = item.get("confidence", 0.8)
            cls = get_confidence_class(conf)

            html += f"""
<div class="card">
<p class="claim">🔹 {item['claim']}</p>
<p class="evidence">Evidence: {item['evidence']}</p>
<p class="{cls}">Confidence: {conf}</p>
</div>
"""

        html += "</div>"

    html += """
</div>
</body>
</html>
"""

    return html


# MARKDOWN
def generate_markdown(groups):
    md = "# Research Digest\n\n"

    for i, group in enumerate(groups):
        if not group:
            continue

        md += f"## Theme {i+1}: {group[0]['claim'][:60]}...\n\n"
        md += f"**Number of Supporting Claims:** {len(group)}\n\n"

        for item in group:
            md += f"### Claim\n{item['claim']}\n\n"
            md += f"**Evidence:** \"{item['evidence']}\"\n\n"
            md += f"**Confidence:** {item.get('confidence', 0.8)}\n\n"
            md += "---\n\n"

    return md


# SAVE OUTPUTS
def save_outputs(groups, sources):
    os.makedirs("outputs", exist_ok=True)

    # Markdown
    md = generate_markdown(groups)
    with open("outputs/digest.md", "w", encoding="utf-8") as f:
        f.write(md)

    # HTML
    html = generate_html(groups)
    with open("outputs/digest.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Sources
    with open("outputs/sources.json", "w", encoding="utf-8") as f:
        json.dump(sources, f, indent=2)

    print("✅ Outputs saved in /outputs (MD + HTML)")