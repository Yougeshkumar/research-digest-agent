import re


def clean_sentence(sent):
    sent = re.sub(r"\[\d+\]", "", sent)  # remove [1], [2]
    sent = sent.replace("\n", " ").strip()
    return sent


def is_valid_sentence(sent):
    return (
        40 <= len(sent) <= 300 and
        "http" not in sent.lower() and
        "privacy" not in sent.lower() and
        "cookie" not in sent.lower() and
        "terms" not in sent.lower() and
        "login" not in sent.lower()
    )


def extract_claims(text, source="unknown"):
    try:
        # Split into sentences
        sentences = re.split(r'(?<=[.!?]) +', text)

        claims = []
        seen = set()  # 🔥 for duplicate removal

        for sent in sentences:
            sent = clean_sentence(sent)

            if not is_valid_sentence(sent):
                continue

            # 🔥 Remove duplicates
            key = sent.lower()
            if key in seen:
                continue
            seen.add(key)

            claims.append({
                "claim": sent,
                "evidence": sent,
                "source": source,
                "confidence": round(min(len(sent) / 150, 1), 2)
            })

        # 🔥 Fallback (if nothing extracted)
        if not claims:
            for sent in sentences[:10]:
                sent = clean_sentence(sent)

                if not sent:
                    continue

                claims.append({
                    "claim": sent,
                    "evidence": sent,
                    "source": source,
                    "confidence": 0.5
                })

        return claims[:10]

    except Exception as e:
        print(f"[ERROR] Extraction failed: {e}")
        return []