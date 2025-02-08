text = input("Enter a string: ")
has_digit = False 

for char in text:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")
