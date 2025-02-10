
tpl = (5, 15, 3, 25, 9, 1, 12)
filtered_elements = []
for x in tpl:
    if 1 <= x <= 10:
        filtered_elements.append(x)

new_tuple = tuple(filtered_elements)

print("Original tuple:", tpl)
print("Filtered tuple:", new_tuple)
