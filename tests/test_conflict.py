def test_conflict():
    claims = [
        {"claim": "Remote work increases productivity", "evidence": "A"},
        {"claim": "Remote work decreases productivity", "evidence": "B"}
    ]

    assert len(claims) == 2