import tkinter as tk
from tkinter import messagebox

# File to store tasks
task_file = "tasks.txt"

def load_tasks():
    """Load tasks from the file"""
    try:
        with open(task_file, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file"""
    with open(task_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    """Add a task to the list"""
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_task_list()
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task before adding.")

def delete_task():
    """Delete the selected task"""
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    """Clear all tasks from the list"""
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_task_list()
        save_tasks(tasks)

def update_task_list():
    """Update the task list display"""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Initialize tasks
tasks = load_tasks()

# Create the main Tkinter window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("600x600")
root.resizable(0,0)
root.configure(bg="#f5f5f5")

# Title label
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Entry widget for new tasks
task_entry_frame = tk.Frame(root, bg="#f5f5f5")
task_entry_frame.pack(pady=10)

task_entry = tk.Entry(task_entry_frame, width=30, font=("Helvetica", 14))
task_entry.pack(side=tk.LEFT, padx=5)

add_task_button = tk.Button(task_entry_frame, text="Add Task", font=("Helvetica", 12), bg="#4caf50", fg="white", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=5)

# Listbox to display tasks
task_listbox_frame = tk.Frame(root, bg="#f5f5f5")
task_listbox_frame.pack(pady=10)

scrollbar = tk.Scrollbar(task_listbox_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(task_listbox_frame, width=40, height=15, font=("Helvetica", 14), yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT)
scrollbar.config(command=task_listbox.yview)

# Populate the listbox with existing tasks
update_task_list()

# Buttons for task actions
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 12), bg="#f44336", fg="white", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=10)

clear_tasks_button = tk.Button(button_frame, text="Clear All", font=("Helvetica", 12), bg="#ff9800", fg="white", command=clear_tasks)
clear_tasks_button.pack(side=tk.LEFT, padx=10)

# Run the Tkinter main loop
root.mainloop()
