def normalize(items):
    return sorted(
        item.replace(' ', '')
            .replace('.doc', '')
            .lower()
        for item in items
    )

# def normalize(items):
#     normalized_items = []
#
#     for item in items:
#         normalized_item = (
#             item.replace(' ', '')
#                 .replace('.doc', '')
#                 .lower()
#         )
#
#         normalized_items.append(normalized_item)
#
#     return sorted(normalized_items)