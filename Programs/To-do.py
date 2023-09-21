class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def show_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i + 1}. {task['task']} - {status}")

# Create a to-do list
my_todo_list = ToDoList()

# Add tasks
my_todo_list.add_task("Write a report")
my_todo_list.add_task("Buy groceries")
my_todo_list.add_task("Read a book")

# Mark a task as completed
my_todo_list.mark_complete(1)

# Display the to-do list
my_todo_list.show_tasks()
