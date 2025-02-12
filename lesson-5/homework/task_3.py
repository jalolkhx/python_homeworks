def factors(n) :
    setFactors = [x for x in range(1,n+1) if n%x == 0]
    return setFactors

num = int(input("Enter a positive integer: "))
for i in factors(num) :
    print(f"{i} is a factor of {num}")