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
        print(f"Processing: {url}")

        data = fetch_url_content(url)
        if not data:
            continue

        claims = extract_claims(data["content"])

        sources_data.append({
            "url": url,
            "claims": claims
        })

        all_claims.extend(claims)

    if not all_claims:
        print("❌ No claims extracted.")
        return

    groups = group_claims(all_claims)

    save_outputs(groups, sources_data)


if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    run_pipeline()