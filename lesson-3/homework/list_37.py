numbers = [13, -1, 17, 11, -12, 12, 3, -3, 3, 14]
sum_of_negatives = 0
for num in numbers:
    if num < 0:
        sum_of_negatives += num

print("Sum of negatives numbers (using loop):", sum_of_negatives)
