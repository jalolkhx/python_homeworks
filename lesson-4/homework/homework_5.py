password = input("Enter your password: ")

# Check length
if len(password) < 8:
    print("Password is too short.")
else:
    # Check for at least one uppercase letter
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    
    if not has_uppercase:
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")
