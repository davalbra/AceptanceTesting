class Task:
    def __init__(self, description, status="Pending"):
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        return [(task.description, task.status) for task in self.tasks]

    def mark_as_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "Completed"

    def mark_as_in_progress(self, description):
      for task in self.tasks:
          if task.description == description:
              task.status = "In Progress"

    def clear(self):
        self.tasks = []

def main():
    todo_list = ToDoList()
    while True:
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Mark a task as in progress")
        print("5. Clear the entire to-do list")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            tasks = todo_list.list_tasks()
            print("Tasks:")
            if len(tasks) == 0:
                print("No tasks")
            else:
                for task, status in tasks:
                    print(f"- {task} ({status})")
        elif choice == "3":
            description = input("Enter the task description to mark as completed: ")
            todo_list.mark_as_completed(description)
        elif choice == "4":
            description = input("Enter the task description to mark as in progress: ")
            todo_list.mark_as_in_progress(description)
        elif choice == "5":
            todo_list.clear()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
