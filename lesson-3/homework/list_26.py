listGiven = [0 ,1, 2, 4, 9, 'qiwi', 'orange']
l = len(listGiven)
if l%2 == 0 :
    m = l//2
    print(listGiven[m-1:m+1])
else :
    m = l//2
    print(listGiven[m])