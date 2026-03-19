import requests
from bs4 import BeautifulSoup

def fetch_url_content(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # ✅ Extract only main article content
        content_div = soup.find("div", {"id": "mw-content-text"})

        if not content_div:
            return None

        paragraphs = content_div.find_all("p")

        # Get only meaningful paragraphs
        text = " ".join([p.get_text() for p in paragraphs if len(p.get_text()) > 50])

        clean_text = " ".join(text.split())

        return {
            "url": url,
            "content": clean_text[:5000]
        }

    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None