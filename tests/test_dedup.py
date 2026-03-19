from src.deduplicate import group_claims

def test_dedup():
    claims = [
        {"claim": "AI is growing fast", "evidence": "x"},
        {"claim": "Artificial intelligence is growing rapidly", "evidence": "y"}
    ]

    groups = group_claims(claims, threshold=0.5)
    assert len(groups) == 1