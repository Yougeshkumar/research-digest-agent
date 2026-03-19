from src.ingest import fetch_url_content

def test_empty():
    result = fetch_url_content("https://invalid-url-test-123.com")
    assert result is None