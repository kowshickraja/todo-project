import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def print_menu():
    print("\n--- To-Do List ---")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Mark Task Done")
    print("4) Delete Task")
    print("5) Clear All Tasks")
    print("0) Exit")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add your first task!")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t.get("done") else "•"
        print(f"{i}. [{status}] {t.get('title')}")

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if not title:
        print("Empty task ignored.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark done: "))
        if 1 <= idx <= len(tasks):
            tasks[idx-1]["done"] = True
            save_tasks(tasks)
            print("Marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx-1)
            save_tasks(tasks)
            print(f"Deleted: {removed.get('title')}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_all(tasks):
    confirm = input("Type 'YES' to clear all tasks: ")
    if confirm == "YES":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Cancelled.")

def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_all(tasks)
        elif choice == "0":
            print("Bye 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__== "__main__":
    main()