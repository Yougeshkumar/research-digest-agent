from collections import defaultdict


def group_claims(claims):
    groups = defaultdict(list)

    for item in claims:
        text = item["claim"].lower()

        if any(word in text for word in [
            "artificial intelligence", "ai", "intelligence", "reasoning"
        ]):
            key = "Artificial Intelligence"

        elif any(word in text for word in [
            "machine learning", "deep learning", "data mining", "algorithm"
        ]):
            key = "Machine Learning"

        elif any(word in text for word in [
            "climate", "global warming", "carbon", "temperature", "environment"
        ]):
            key = "Climate Change"

        elif any(word in text for word in [
            "electric vehicle", "ev", "battery", "motor", "vehicle"
        ]):
            key = "Electric Vehicles"

        elif any(word in text for word in [
            "remote work", "work from home", "telework", "office", "workplace"
        ]):
            key = "Remote Work"

        else:
            # 🔥 REMOVE weak claims instead of dumping into "Other"
            continue

        groups[key].append(item)

    # Convert to final structure
    final_groups = []

    for key, items in groups.items():
        if len(items) < 2:
            continue  # 🔥 remove weak themes

        final_groups.append({
            "theme": key,
            "claims": items[:5]
        })

    return final_groups