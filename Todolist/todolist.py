import tkinter as tk

# jendela utama
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x600")
root.config(bg="#f7e1e1")

# Label Judul
title_label = tk.Label(root, text="To-Do List", font=("Times New Roman", 24, "bold"), bg="#f7e1e1", fg="#333")
title_label.pack(pady=20)

# Listbox untuk menampilkan daftar tugas
task_listbox = tk.Listbox(root, font=("Times New Roman", 14), width=30, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Fungsi untuk menambahkan tugas
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Fungsi untuk menandai tugas selesai
def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, {'fg': 'gray', 'font': ('Times New Roman', 14, 'italic')})
    except IndexError:
        pass  # Tidak ada tugas yang dipilih

# Fungsi untuk menghapus semua tugas
def delete_all():
    task_listbox.delete(0, tk.END)

# Entry untuk menambahkan tugas baru
task_entry = tk.Entry(root, font=("Times New Roman", 14), width=30)
task_entry.pack(pady=10)

# Tombol untuk menambahkan tugas
add_button = tk.Button(root, text="Tambah Tugas", font=("Times New Roman", 14), command=add_task, bg="#FFB6C1", fg="black", relief="solid", bd=1)
add_button.pack(pady=10)

# Tombol untuk menandai tugas selesai
done_button = tk.Button(root, text="Tandai Selesai", font=("Times New Roman", 14), command=mark_done, bg="#FFB6C1", fg="black", relief="solid", bd=1)
done_button.pack(pady=10)

# Tombol untuk menghapus semua tugas
delete_button = tk.Button(root, text="Hapus Semua", font=("Times New Roman", 14), command=delete_all, bg="#FFB6C1", fg="black", relief="solid", bd=1)
delete_button.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()

