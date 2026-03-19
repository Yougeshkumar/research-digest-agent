import re

def extract_claims(text):
    try:
        # Split into sentences
        sentences = re.split(r'(?<=[.!?]) +', text)

        claims = []

        for sent in sentences:
            # Clean sentence
            sent = re.sub(r"\[\d+\]", "", sent)  # remove [1], [2]
            sent = sent.strip().replace("\n", " ")

            # Skip garbage / weak sentences
            if (
                len(sent) < 40 or
                len(sent) > 300 or
                "http" in sent.lower() or
                "wiki" in sent.lower() or
                "privacy" in sent.lower() or
                "cookie" in sent.lower()
            ):
                continue

            claims.append({
                "claim": sent,
                "evidence": sent,
                "confidence": round(min(len(sent) / 150, 1), 2)
            })

        # Fallback if everything filtered out
        if not claims:
            for sent in sentences[:10]:
                sent = sent.strip().replace("\n", " ")
                claims.append({
                    "claim": sent,
                    "evidence": sent,
                    "confidence": 0.5
                })

        return claims[:10]

    except Exception as e:
        print(f"[ERROR] Local extraction failed: {e}")
        return []