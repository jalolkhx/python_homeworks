set1 = set()
for i in range(2,100) :
    for k in range(2, i) :
        if i % k == 0 :
            set1.add(i)
            break

setOfPrime = set(range(2,100)) - set1
print(setOfPrime)