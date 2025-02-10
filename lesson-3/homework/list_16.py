numbers = [1,2,3,4,5,6,7,8,9,10,20,25]
oddNum = 0
for i in numbers :
    if i%2==1 :
        oddNum=oddNum+1
    
print(f"number of odd elements in the list is {oddNum}")