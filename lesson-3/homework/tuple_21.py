tuple1 = (4,6,7,3,8,12,-1)
givenNumber = 3
list1 = []
for i in range(len(tuple1)) :
    for k in range(3) :
        list1.append(tuple1[i])

newTuple = tuple(list1)
print(newTuple)
