import tkinter as tk
from tkinter import Menu, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Productivity Toolkit")
        self.root.geometry("300x400")
        self.root.config(bg="#f4f4f4")

        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_info)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        label = tk.Label(self.root, text="Kalkulator Sederhana", font=("Arial", 16), bg="#f4f4f4", fg="#333")
        label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 18), borderwidth=5, relief=tk.SUNKEN, justify='right')
        self.entry.pack(pady=10, padx=10, fill=tk.X)

        button_frame = tk.Frame(self.root, bg="#f4f4f4")
        button_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == "C":
                button = tk.Button(button_frame, text=text, font=("Arial", 14), bg="#ffadad", fg="white",
                                   padx=20, pady=10, command=self.clear_entry)
            elif text == "=":
                button = tk.Button(button_frame, text=text, font=("Arial", 14), bg="#77dd77", fg="white",
                                   padx=20, pady=10, command=self.calculate)
            else:
                button = tk.Button(button_frame, text=text, font=("Arial", 14), bg="#dcdcdc", fg="black",
                                   padx=20, pady=10, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(number))

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            messagebox.showerror("Error", "Invalid Input")

    def show_info(self):
        messagebox.showinfo("About", "Student Productivity Toolkit\nFitur: Kalkulator Sederhana\nDibuat dengan Python dan Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
