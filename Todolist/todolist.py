import tkinter as tk

class Todolist:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x600")
        self.root.config(bg="#f7e1e1")

        tk.Label(root, text="To-Do List", font=("Times New Roman", 24, "bold"), bg="#f7e1e1", fg="#333").pack(pady=20)

        self.task_listbox = tk.Listbox(root, font=("Times New Roman", 14), width=30, height=10)
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Times New Roman", 14), width=30)
        self.task_entry.pack(pady=10)

        self.create_button("Tambah Tugas", self.add_task)
        self.create_button("Tandai Selesai", self.mark_done)
        self.create_button("Hapus Semua", self.delete_all)

    def create_button(self, text, command):
        tk.Button(self.root, text=text, font=("Times New Roman", 14), command=command, bg="#FFB6C1", fg="black").pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_done(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.itemconfig(selected, {'fg': 'gray', 'font': ('italic', 14)})
        except IndexError:
            pass

    def delete_all(self):
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    Todolist(root)
    root.mainloop()
