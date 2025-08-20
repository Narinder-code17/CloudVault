# Simple To-Do List App (Dictionary Based)1

tasks = {}
task_id = 1

# Function to add task
def add_task(description):
    global task_id
    tasks[task_id] = {"description": description, "completed": False}
    print(f"Task '{description}' added successfully with ID {task_id}")
    task_id += 1

# Function to mark task as completed
def mark_done(tid):
    if tid in tasks:
        tasks[tid]["completed"] = True
        print(f"Task ID {tid} marked as completed ✅")
    else:
        print("Invalid Task ID ❌")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    print("\nYour Tasks:")
    for tid, task in tasks.items():
        status = "✅ Completed" if task["completed"] else "❌ Pending"
        print(f"{tid}. {task['description']} - {status}")
    print()

# Main program loop
while True:
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        desc = input("Enter task description: ")
        add_task(desc)
    elif choice == "2":
        tid = int(input("Enter Task ID to mark completed: "))
        mark_done(tid)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting To-Do List App. Goodbye 👋")
        break
    else:
        print("Invalid choice! Please select 1-4.")
