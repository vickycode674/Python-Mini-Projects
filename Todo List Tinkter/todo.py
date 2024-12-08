import tkinter as tk
from tkinter import messagebox

# Functionality for To-Do List
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#f4f4f4")

        # Task List
        self.tasks = []

        # Title Label
        tk.Label(self.root, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

        # Task Input Frame
        self.task_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.task_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.task_frame, font=("Helvetica", 14), width=25, bd=1, relief=tk.SOLID)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(
            self.task_frame,
            text="Add",
            font=("Helvetica", 12),
            bg="#5cb85c",
            fg="white",
            activebackground="#4cae4c",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.add_task
        )
        self.add_button.grid(row=0, column=1)

        # Task Display Frame
        self.list_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.list_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            self.list_frame,
            font=("Helvetica", 14),
            width=30,
            height=15,
            bg="#ffffff",
            fg="#333",
            bd=1,
            relief=tk.SOLID,
            selectbackground="#5cb85c",
            selectforeground="white"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Action Buttons Frame
        self.button_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.button_frame.pack(pady=10)

        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete",
            font=("Helvetica", 12),
            bg="#d9534f",
            fg="white",
            activebackground="#c9302c",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.delete_task
        )
        self.delete_button.grid(row=0, column=0, padx=10)

        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear All",
            font=("Helvetica", 12),
            bg="#f0ad4e",
            fg="white",
            activebackground="#ec971f",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.clear_tasks
        )
        self.clear_button.grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task.strip() == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "No task selected to delete!")

    def clear_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()