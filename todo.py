tasks = []

def show_menu():
    print("\nTodo List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: "))
        tasks.pop(index - 1)
        print("Task removed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
