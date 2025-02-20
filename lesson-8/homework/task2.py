import random
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def making_dict(self):
        dict1 = {}
        dict1['Account Number'] = self.account_number
        dict1['Name'] = self.name
        dict1['Balance'] = self.balance
        return dict1
    
    def __str__(self):
        return f"{self.account_number}, {self.name}, {self.balance}"

class Bank():
    def __init__(self):
       self.accounts = {}

    def generate_number(self):
       return random.randint(10000,99999)
    
    def create_account(self, name, initial_deposite):
        a = len(self.accounts)+1
        account_number = self.generate_number()
        user = Account(account_number, name, initial_deposite)
        self.accounts[a] = user.making_dict()
        with open('notebook.txt', 'a') as f:
            f.write(str(user) + '\n')

        print(f"Account is created successfully\n Your account number is {account_number}")

    def view_account(self, account_number):
        found = False
        with open('notebook.txt', 'r') as f:
            for i in f.readlines():
                if i.startswith(str(account_number)):
                    found = True
                    print(i)
                    break
        if not found:
            print("The account number is not found! ")

    def deposit(self, account_number, amount: int):
        found = False
        with open('notebook.txt', 'r') as f:
            lines = f.readlines()
        with open('notebook.txt', 'w') as f:
            for i in lines:
                if not i.startswith(str(account_number)):
                    f.write(i)
                else:
                    found = True
                    tuple1 = i.split(', ')
                    balance = int(tuple1[-1])
                    balance += amount
                    str1 = ' ,'.join(tuple1[:-1])
                    f.write(f"{str1}, {balance}\n")
                    
        for k, i in self.accounts.items():
            if i['Account Number'] == account_number:
                i['Balance'] += amount
                print("Deposit is made successfully!")
                break
        if not found:
            print("The account number is not found! ")

    def withdraw(self, account_number, amount: int):
        found = False
        with open('notebook.txt', 'r') as f:
            lines = f.readlines()
        with open('notebook.txt', 'w') as f:
            for i in lines:
                if not i.startswith(str(account_number)):
                    f.write(i)
                else:
                    found = True
                    tuple1 = i.split(', ')
                    balance = int(tuple1[-1])
                    if balance < amount:
                        print("Insufficient balance!")
                        return
                    balance -= amount
                    str1 = ' ,'.join(tuple1[:-1])
                    f.write(f"{str1}, {balance}\n")
                    
        for k, i in self.accounts.items():
            if i['Account Number'] == account_number:
                i['Balance'] -= amount
                print("Withdraw is made successfully!")
                break
        if not found:
            print("The account number is not found! ")
