tuple1 = (1,2,3,88,56,56,'apple')
list1 = []
for i in tuple1 :
    if tuple1.count(i) == 1 :
        list1.append(i)

newTuple = tuple(list1)
print(f"Unique elements in the tuple {newTuple}")