import os
from ingest import fetch_url_content
from extract import extract_claims
from deduplicate import group_claims
from generate import save_outputs


def load_urls(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def run_pipeline():
    urls = load_urls("data/input_urls.txt")

    all_claims = []
    sources_data = []

    for url in urls:
        print(f"🔄 Processing: {url}")

        data = fetch_url_content(url)
        if not data:
            print(f"⚠️ Skipped (no data): {url}")
            continue

        # ✅ FIX: pass source (VERY IMPORTANT)
        claims = extract_claims(data["content"], url)

        sources_data.append({
            "url": url,
            "claims": claims
        })

        all_claims.extend(claims)

    if not all_claims:
        print("❌ No claims extracted.")
        return

    print(f"✅ Total Claims Extracted: {len(all_claims)}")

    groups = group_claims(all_claims)

    print(f"🧠 Total Themes Generated: {len(groups)}")

    save_outputs(groups, sources_data)

    print("🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    run_pipeline()