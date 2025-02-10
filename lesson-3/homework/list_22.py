numbers = [1,2,3,4,5,6,7,8,9,10,20,25]
evenNum = []
for i in numbers :
    if i%2==0 :
        evenNum.append(i)
    
print(f"list of even elements in the list is {evenNum}")