list1 = []
def addEmployee(ID, Name, Position, Salary) :
    dict1 = {'ID' : ID, 
             'Name' : Name, 
             'Position' : Position, 
             'Salary' : Salary }
    list1.append(dict1)
    with open('employees.txt', 'w') as f:
        for i in list1 :
            str_dict = ", ".join(f"{value}" for value in i.values())
            f.write(str_dict + '\n')
        print("Employee added successfully!")

def allRecords() :
    with open('employees.txt', 'r') as f:
        return f.read()

def Search(ID) :
    with open('employees.txt', 'r') as f:
        boolean1 = False
        for i in list1 :
            if i['ID'] == ID :
                str_dict = " ,".join(f"{value}" for value in i.values())
                print(str_dict)
                boolean1 = True
                break
            
        if boolean1 == False :
            print("No match ID found")

def Update(ID) :
    Search(ID)
    for i in list1 :
        if i['ID'] == ID :
            new_name = input("Enter new name: ")
            new_position = input("Enter new position: ")
            new_salary = int(input("Enter new salary: "))
            i['Name'] = new_name
            i['Position'] = new_position
            i['Salary'] = new_salary

            with open('employees.txt', 'wt') as f:
                for i in list1 :
                    str_dict = ", ".join(f"{value}" for value in i.values())
                    f.write(str_dict + '\n')
            break
            
    print("Information is changed successfully")

def Delate(ID) :
    for i in list1 :
        if i['ID'] == ID :
            list1.remove(i)
        
            with open('employees.txt', 'wt') as f:
                for k in list1 :
                    str_dict = ", ".join(f"{value}" for value in k.values())
                    f.write(str_dict + '\n')
                    print("Delated!")
                    break

while True:
    input1 = int(input("1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n"))
    if input1 == 1 :
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = int(input("Enter salary: "))

        addEmployee(id, name, position, salary)
    elif input1 == 2 :
        print(allRecords())
    elif input1 == 3 :
        id = int(input("Enter an ID: "))
        Search(id)
    elif input1 == 4 :
        id = int(input("Enter an ID: "))
        Update(id)
    elif input1 == 5 :
        id = int(input("Enter an ID: "))
        Delate(id)
    elif input1 == 6 :
        quit()
    else :
        print("Incorrect number entered! ")
    


            

