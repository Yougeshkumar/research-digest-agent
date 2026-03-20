import json
import os


def get_confidence_class(conf):
    if conf >= 0.8:
        return "high"
    elif conf >= 0.5:
        return "medium"
    else:
        return "low"


# ================= SUMMARY GENERATOR =================
def generate_summary(claims):
    if not claims:
        return ""

    important = claims[:3]
    sentences = [c["claim"] for c in important]

    summary = " ".join(sentences)

    return summary[:200] + "..." if len(summary) > 200 else summary


# ================= HTML GENERATOR =================
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
                padding: 20px;
                background: #0f172a;
                color: #e2e8f0;
            }

            h1 {
                font-size: 32px;
                margin-bottom: 20px;
            }

            input {
                width: 100%;
                padding: 12px;
                margin-bottom: 20px;
                border-radius: 8px;
                border: none;
                outline: none;
                font-size: 16px;
            }

            .theme {
                margin-top: 30px;
            }

            .theme-header {
                background: linear-gradient(135deg, #6366f1, #8b5cf6);
                padding: 15px;
                border-radius: 10px;
            }

            .summary {
                margin-top: 10px;
                font-size: 14px;
                color: #e0e7ff;
            }

            .sources {
                font-size: 13px;
                margin-top: 8px;
                color: #cbd5f5;
            }

            .card {
                background: #1e293b;
                padding: 15px;
                margin: 12px 0;
                border-radius: 10px;
                border-left: 4px solid #6366f1;
            }

            .claim {
                font-weight: 600;
            }

            .evidence {
                font-size: 14px;
                color: #94a3b8;
                margin-top: 5px;
            }

            .high { color: #22c55e; }
            .medium { color: #f59e0b; }
            .low { color: #ef4444; }
        </style>
    </head>

    <body>

        <h1>📊 Research Digest</h1>

        <!-- 🔍 THEME SEARCH BAR -->
        <input 
            type="text" 
            id="themeSearch" 
            placeholder="🔍 Search themes..." 
            onkeyup="filterThemes()"
        >
    """

    for i, group in enumerate(groups):
        if not group or not group["claims"]:
            continue

        sources = list(set([item.get("source", "Unknown") for item in group["claims"]]))
        summary = generate_summary(group["claims"])

        html += f"""
        <div class="theme searchable-theme">
            <div class="theme-header">
                <b>🧠 Theme {i+1}</b><br>
                <span class="theme-title">{group['theme']}</span><br>

                <div class="summary">
                    🤖 <b>Summary:</b> {summary}
                </div>

                <div class="sources">
                    🔗 Sources: {", ".join(sources)}
                </div>
            </div>
        """

        for idx, item in enumerate(group["claims"], 1):
            conf = item.get("confidence", 0.8)
            cls = get_confidence_class(conf)

            html += f"""
            <div class="card">
                <p class="claim">🔹 <b>Claim {idx}:</b> {item['claim']}</p>
                <p class="evidence"><b>Evidence:</b> {item['evidence'][:120]}...</p>
                <p class="{cls}"><b>Confidence:</b> {conf}</p>
            </div>
            """

        html += "</div>"

    # 🔥 JAVASCRIPT FOR THEME SEARCH
    html += """
    <script>
    function filterThemes() {
        let input = document.getElementById("themeSearch").value.toLowerCase();
        let themes = document.getElementsByClassName("searchable-theme");

        for (let i = 0; i < themes.length; i++) {
            let title = themes[i].getElementsByClassName("theme-title")[0];
            let text = title.innerText.toLowerCase();

            if (text.includes(input)) {
                themes[i].style.display = "block";
            } else {
                themes[i].style.display = "none";
            }
        }
    }
    </script>
    """

    html += "</body></html>"

    return html


# ================= MARKDOWN GENERATOR =================
def generate_markdown(groups):
    md = "# Research Digest\n\n"

    for i, group in enumerate(groups):
        if not group or not group["claims"]:
            continue

        sources = list(set([item.get("source", "Unknown") for item in group["claims"]]))
        summary = generate_summary(group["claims"])

        md += f"## Theme {i+1}: {group['theme']}\n\n"
        md += f"**Summary:** {summary}\n\n"
        md += f"**Sources:** {', '.join(sources)}\n\n"

        for idx, item in enumerate(group["claims"], 1):
            md += f"- **Claim {idx}:** {item['claim']}\n"
            md += f"  - Evidence: \"{item['evidence'][:120]}...\"\n"
            md += f"  - Confidence: {item.get('confidence', 0.8)}\n\n"

        md += "---\n\n"

    return md


# ================= SAVE OUTPUTS =================
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

    # JSON
    with open("outputs/sources.json", "w", encoding="utf-8") as f:
        json.dump(sources, f, indent=2)

    print("✅ Outputs saved in /outputs (HTML + MD + JSON)")