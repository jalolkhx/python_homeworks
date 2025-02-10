numbers = [1, 2, 3, 2, 4, 2, 5]
element = 2

indices = []
for i in range(len(numbers)):
    if numbers[i] == element:
        indices.append(i)

print(f"Indices of {element}: {indices}")
