#!/usr/bin/python3

items = [
        ("product_name1", 10),
        ("product_name2", 5),
        ("product_name3", 15),
        ("product_name4", 20)
        ]

filtered = []

for item in items:
	if item[1] >= 10:
		filtered.append(item[1])
print(filtered)
