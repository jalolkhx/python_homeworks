class Task:
    def __init__(self, Task_ID, Title, Description, task_data, task_status):
        self.task_ID = str(Task_ID)  # Ensuring ID is always a string
        self.title = Title
        self.description = Description
        self.task_data = task_data
        self.status = task_status

    def __str__(self):
        return f"{self.task_ID}, {self.title}, {self.description}, {self.task_data}, {self.status}"
    
class FuncTask:
    def __init__(self, file='notebook.txt'):
        self.file = file

    def add_task(self, task: Task):
        with open(self.file, 'a') as f:
            f.write(str(task) + '\n')
        print("Task added successfully!")

    def view_tasks(self):
        try:
            with open(self.file, 'r') as f:
                records = f.readlines()
                if records:
                    print("Task Records:")
                    for record in records:
                        print(record.strip())
                else:
                    print("No tasks found.")
        except FileNotFoundError:
            print("No task records found. The file does not exist.")

    def update_task(self, Task_ID, Title=None, Description=None, task_data=None, task_status=None):
        updated_tasks = []
        found = False

        try:
            with open(self.file, 'r') as f:
                for line in f.readlines():
                    task_parts = line.strip().split(', ')

                    if task_parts[0] == str(Task_ID):  # Ensure matching with string ID
                        found = True
                        if Title:
                            task_parts[1] = Title
                        if Description:
                            task_parts[2] = Description
                        if task_data:
                            task_parts[3] = task_data
                        if task_status:
                            task_parts[4] = task_status

                        updated_tasks.append(', '.join(task_parts) + '\n')
                    else:
                        updated_tasks.append(line)

            if found:
                with open(self.file, 'w') as f:
                    f.writelines(updated_tasks)
                print("Task information updated successfully!")
            else:
                print("Task not found!")

        except FileNotFoundError:
            print("No task records found. The file does not exist.")

    def delete_task(self, Task_ID):
        updated_tasks = []
        found = False

        try:
            with open(self.file, 'r') as f:
                for line in f.readlines():
                    if not line.startswith(str(Task_ID)):  # Ensuring ID comparison works
                        updated_tasks.append(line)
                    else:
                        found = True

            if found:
                with open(self.file, 'w') as f:
                    f.writelines(updated_tasks)
                print("Task deleted successfully!")
            else:
                print("Task not found!")

        except FileNotFoundError:
            print("No task records found. The file does not exist.")

    def filter_tasks(self):
        try:
            with open(self.file, 'r') as f:
                tasks = [line.strip() for line in f.readlines()]
            
            if not tasks:
                print("No tasks to filter.")
                return

            # Sorting by task status (assuming status is at the last position)
            sorted_tasks = sorted(tasks, key=lambda k: k.split(', ')[-1])

            print("Tasks Sorted by Status:")
            for task in sorted_tasks:
                print(task)

        except FileNotFoundError:
            print("No task records found. The file does not exist.")
        except ValueError:
            print("Task data is incorrectly formatted, unable to sort.")

todo = FuncTask()

while True:
    print("\nWelcome to the To-Do Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Filter tasks by status")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        todo.add_task(Task(task_id, title, description, due_date, status))

    elif choice == "2":
        todo.view_tasks()

    elif choice == "3":
        task_id = input("Enter Task ID to update: ")
        title = input("New Title (leave blank to keep unchanged): ") or None
        description = input("New Description (leave blank to keep unchanged): ") or None
        due_date = input("New Due Date (YYYY-MM-DD, leave blank to keep unchanged): ") or None
        status = input("New Status (Pending/In Progress/Completed, leave blank to keep unchanged): ") or None
        todo.update_task(task_id, title, description, due_date, status)

    elif choice == "4":
        task_id = input("Enter Task ID to delete: ")
        todo.delete_task(task_id)

    elif choice == "5":
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        todo.filter_tasks(status)

    elif choice == "8":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")