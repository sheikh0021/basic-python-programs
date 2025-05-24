class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added : {task}")
    
    def view_task(self):
        if not self.tasks:
            print("No tasks in your to-do list")
            return
        
        print("\n Your todolist :")
        for i, task in enumerate(self.tasks, 1):
            status = "done" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

    def mark_complete(self, task_number):
        if 1 <= task_number <=len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed")
        else:
            print("Invalid task number")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number")

    def clear_all(self):
        self.tasks = []
        print("All tasks cleared")

def main():
    todo = ToDoList()

    while True:
        print("\nTodo-list Menu :")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Test as Completed")
        print("4. Delete Task")
        print("5. Clear all tasks")
        print("6. Exit")

        choice = input("Enter your choice here : ")
        if choice == "1":
           task = input("Enter the task: ")
           todo.add_task(task)
        
        elif choice == "2":
            todo.view_task()

        elif choice == "3":
            todo.view_task()
            task_num = int(input("Enter the number to mark complete :"))
            todo.mark_complete(task_num)
        
        elif choice == "4":
            todo.view_task()
            task_num = int(input("Enter the number to mark delete :"))
            todo.delete_task(task_num)

        elif choice == "5":
            confirm = input("Are you sure you want to clear all tasks? (y/n): ")
            if confirm.lower() == "y":
                todo.clear_all()
        
        elif choice == "6":
            print("Goodbyee")
            break
        else: 
            print("Invalid choice. Try again")

main()