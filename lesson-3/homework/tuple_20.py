tuple1 = (4,6,7,3,8,12,-1)
list1 = []
l=len(tuple1)
for i in range(l-3) :
    list1.append(tuple1[i:i+3])

newTuple = tuple(list1)
print(newTuple)
