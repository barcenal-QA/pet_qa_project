def normalize(items):
    return sorted(
        item.replace(' ', '')
            .replace('.doc', '')
            .lower()
        for item in items
    )