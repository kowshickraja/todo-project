import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILENAME = "tasks.json"

# ----------- Save & Load Functions -----------
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

# ----------- Core Functions -----------
def add_task():
    task = entry.get()
    if task != "":
        priority = simpledialog.askstring("Priority", "Enter priority (High/Medium/Low):")
        due_date = simpledialog.askstring("Due Date", "Enter due date (e.g. 2025-08-30):")

        new_task = {
            "task": task,
            "completed": False,
            "priority": priority if priority else "None",
            "due_date": due_date if due_date else "None"
        }

        tasks.append(new_task)
        update_listbox()
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = not tasks[index]["completed"]  # Toggle complete
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to mark complete!")

# ----------- GUI Helper -----------
def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t['completed'] else "❌"
        display_text = f"{status} {t['task']} [Priority: {t['priority']}] [Due: {t['due_date']}]"
        listbox.insert(tk.END, display_text)

# ----------- Main Window -----------
root = tk.Tk()
root.title("To-Do App (GUI)")
root.geometry("500x500")

# Input
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Complete", command=mark_completed)
complete_button.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# Load old tasks
tasks = load_tasks()
update_listbox()

root.mainloop()