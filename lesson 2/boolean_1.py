import sys
user = input("Enter your username: ")
if user == "" :
    print("username cannot be empty, try again")
    sys.exit()

password = input("Enter your password: ")
if password == "" :
    print("password cannot be empty, try again")
    sys.exit()