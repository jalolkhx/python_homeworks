class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    def __init__(self, filename='employees.txt'):
        self.filename = filename

    def add_employee(self, employee: Employee):
        with open(self.filename, 'a') as file:
            file.write(str(employee) + '\n')
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()
                if records:
                    print("Employee Records:")
                    for record in records:
                        print(record.strip())
                else:
                    print("No employee records found.")
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()
                for record in records:
                    if record.startswith(employee_id):
                        print("Employee Found:")
                        print(record.strip())
                        return
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated_records = []
        found = False
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()
                for record in records:
                    if record.startswith(employee_id):
                        found = True
                        emp_data = record.strip().split(', ')
                        if name:
                            emp_data[1] = name
                        if position:
                            emp_data[2] = position
                        if salary:
                            emp_data[3] = salary
                        updated_records.append(', '.join(emp_data) + '\n')
                    else:
                        updated_records.append(record)
            if found:
                with open(self.filename, 'w') as file:
                    file.writelines(updated_records)
                print("Employee information updated successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self, employee_id):
        updated_records = []
        found = False
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()
                for record in records:
                    if not record.startswith(employee_id):
                        updated_records.append(record)
                    else:
                        found = True
            if found:
                with open(self.filename, 'w') as file:
                    file.writelines(updated_records)
                print("Employee record deleted successfully!")
            else:
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(employee_id, name, position, salary)
                self.add_employee(employee)
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == '4':
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to keep current): ")
                position = input("Enter new Position (leave blank to keep current): ")
                salary = input("Enter new Salary (leave blank to keep current): ")
                self.update_employee(employee_id, name if name else None,
                                     position if position else None,
                                     salary if salary else None)
            elif choice == '5':
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


