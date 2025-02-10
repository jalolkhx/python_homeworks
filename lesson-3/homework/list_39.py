numbers = [13, -1, 17, 11, -12, 12, 3, -3, 3, 14]
chunk_size = 3
nested_list = []
for i in range(0, len(numbers), chunk_size):
    nested_list.append(numbers[i:i + chunk_size])

print("Nested list (using loop):", nested_list)
