def check(orgFunction) :
    def wrapped(a,b) :
        try:
            return orgFunction(a,b)
        except ZeroDivisionError:
            return "Denominator can't be zero"
    
    return wrapped

@check
def div(a, b) :
    return a / b

x = float(input("Input 1: "))
y = float(input("Input 2: "))
print(div(x,y))