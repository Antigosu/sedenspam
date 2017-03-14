from openpyxl import load_workbook

# e-mail input area
spam_file = load_workbook(filename=r'.\spam_base.xlsx', read_only=False)
spam_base = spam_file['spam_base']
cache = {}
templates = {}
row_number = -1

for row in spam_base.rows:
    row_number += 1
    template = []
    for cell in row:
        if cell.value:
            template.append(cell.value)
    cache.setdefault(row_number, template)

for key in cache.keys():
    if cache[key]:
        templates.setdefault(key, cache[key])

print(templates)