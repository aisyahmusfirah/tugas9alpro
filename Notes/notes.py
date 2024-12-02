import tkinter as tk
from tkinter import Menu, messagebox, simpledialog, filedialog

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")

def show_info():
    messagebox.showinfo("About", "Student Productivity Toolkit\nFitur: Kalkulator Sederhana dan Notes\nDibuat dengan Python dan Tkinter.")

def open_notes():
    global notes_window
    notes_window = tk.Toplevel(root)
    notes_window.title("Notes")
    notes_window.geometry("400x300")
    notes_window.config(bg="#f4f4f4")

    notes_label = tk.Label(notes_window, text="Catatan Anda", font=("Arial", 14), bg="#f4f4f4", fg="#333")
    notes_label.pack(pady=5)

    global text_area
    text_area = tk.Text(notes_window, wrap=tk.WORD, font=("Arial", 12), width=40, height=10)
    text_area.pack(pady=10, padx=10)

    save_button = tk.Button(notes_window, text="Simpan", font=("Arial", 12), bg="#77dd77", fg="white", command=save_notes)
    save_button.pack(pady=5)

    load_button = tk.Button(notes_window, text="Buka", font=("Arial", 12), bg="#77dd77", fg="white", command=load_notes)
    load_button.pack(pady=5)

def save_notes():
    notes_content = text_area.get("1.0", tk.END).strip()
    if notes_content:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(notes_content)
            messagebox.showinfo("Success", "Catatan berhasil disimpan!")
    else:
        messagebox.showwarning("Warning", "Catatan kosong! Tidak ada yang disimpan.")

def load_notes():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            notes_content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, notes_content)
        messagebox.showinfo("Success", "Catatan berhasil dimuat!")

root = tk.Tk()
root.title("Student Productivity Toolkit")
root.geometry("300x400")
root.config(bg="#f4f4f4")

menu_bar = Menu(root)
root.config(menu=menu_bar)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_info)
menu_bar.add_cascade(label="Help", menu=help_menu)

notes_menu = Menu(menu_bar, tearoff=0)
notes_menu.add_command(label="Open Notes", command=open_notes)
menu_bar.add_cascade(label="Notes", menu=notes_menu)

label = tk.Label(root, text="Kalkulator Sederhana", font=("Arial", 16), bg="#f4f4f4", fg="#333")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.SUNKEN, justify='right')
entry.pack(pady=10, padx=10, fill=tk.X)

button_frame = tk.Frame(root, bg="#f4f4f4")
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
                           padx=20, pady=10, command=clear_entry)
    elif text == "=":
        button = tk.Button(button_frame, text=text, font=("Arial", 14), bg="#77dd77", fg="white",
                           padx=20, pady=10, command=calculate)
    else:
        button = tk.Button(button_frame, text=text, font=("Arial", 14), bg="#dcdcdc", fg="black",
                           padx=20, pady=10, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
