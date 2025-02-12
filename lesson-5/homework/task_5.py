def is_prime(n) :
    if n in [2,3] :
        return True
    else:
        boolean1 = True
        for i in range(2,n//2) :
            if n%i==0 :
                boolean1 = False
                break
        return boolean1
    
number = int(input("Enter a integer number: "))
print(is_prime(number))