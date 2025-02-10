numbers = [1, 2, 3, 4, 5]
k = 2 

k = k % len(numbers)
rotated_list = numbers[-k:] + numbers[:-k]

print("Rotated list:", rotated_list)
