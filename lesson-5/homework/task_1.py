def convert_cel_to_far(celsius) :
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit) :
    return (fahrenheit - 32) * 5/9

F = float(input("Enter a temperature in degrees F: "))
print(f"{F} degrees F = {convert_far_to_cel(F):.2f} defrees C")

C = float(input("Enter a temperature in degrees C: "))
print(f"{C} degrees C = {convert_cel_to_far(C):.2f} defrees F")
