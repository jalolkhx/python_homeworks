numbers1 = [1, 5, 3, 9, 2, 8, 7]
numbers2 = [1, 4, 6, 9, 0, -1, -7]
numMerge = numbers1 + numbers2
numMerge.sort()
print("Merged and sorted: ", numMerge)
# or 2-solution
numbers1 = [1, 5, 3, 9, 2, 8, 7]
numbers2 = [1, 4, 6, 9, 0, -1, -7]
numbers1.extend(numbers2)
numbers1.sort()
print(numbers1)