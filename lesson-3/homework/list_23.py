numbers = [1,2,3,4,5,6,7,8,9,10,20,25]
oddNum = []
for i in numbers :
    if i%2==1 :
        oddNum.append(i)
    
print(f"list of odd elements in the list is {oddNum}")