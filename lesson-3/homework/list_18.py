list1 = [1,2,3,4,5,6,7,8,9]
subList = [4,5,6]
a = len(subList)
b = len(list1)
bool_1 = False
for i in range(0,b-a+1) :
    if subList == list1[i:i+a] :
        bool_1 = True

print(f"is {subList} sublist of {list1}? ", bool_1)