set1 = {1,2,3,4,5,6,77,8}
set2 = set()
for i in set1 :
    if i % 2 == 0 :
        set2.add(i)

print("even elements of set: ", set2)