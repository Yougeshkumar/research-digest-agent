def group_claims(claims):
    groups = {}

    for item in claims:
        text = item["claim"].lower()

        # 🔹 Simple topic detection
        if "artificial intelligence" in text or "ai" in text:
            key = "Artificial Intelligence"

        elif "climate" in text or "global warming" in text:
            key = "Climate Change"

        elif "electric vehicle" in text or "ev" in text:
            key = "Electric Vehicles"

        elif "remote work" in text or "work from home" in text:
            key = "Remote Work"

        elif "machine learning" in text:
            key = "Machine Learning"

        else:
            key = "Other Insights"

        if key not in groups:
            groups[key] = []

        groups[key].append(item)

    return list(groups.values())