import tkinter as tk
from tkinter import Menu, messagebox

# Fungsi Operasi Kalkulator
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  # Menghitung ekspresi matematika
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")

# Fungsi untuk informasi aplikasi
def show_info():
    messagebox.showinfo("About", "Student Productivity Toolkit\nFitur: Kalkulator Sederhana\nDibuat dengan Python dan Tkinter.")

# Membuat Window Utama
root = tk.Tk()
root.title("Student Productivity Toolkit")
root.geometry("300x400")
root.config(bg="#f4f4f4")

# Menu Navigasi
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Menambahkan Menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_info)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Tampilan Kalkulator
label = tk.Label(root, text="Kalkulator Sederhana", font=("Arial", 16), bg="#f4f4f4", fg="#333")
label.pack(pady=10)

# Entry Widget untuk Input dan Output
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.SUNKEN, justify='right')
entry.pack(pady=10, padx=10, fill=tk.X)

# Frame untuk Tombol
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack()

# Daftar Tombol (Grid)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Membuat dan Memasukkan Tombol ke dalam Grid
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

# Menjalankan Aplikasi
root.mainloop()

