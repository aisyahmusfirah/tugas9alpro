import tkinter as tk
from tkinter import messagebox, filedialog

class Notes:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan anda")
        self.root.geometry("400x400")
        self.root.config(bg="#f4f4f4")
        
        self.create_notes_section()

    def create_notes_section(self):
        notes_label = tk.Label(self.root, text="Catatan Anda", font=("Arial", 14), bg="#f4f4f4", fg="#333")
        notes_label.pack(pady=5)

        self.text_area = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12), width=40, height=10)
        self.text_area.pack(pady=10, padx=10)

        save_button = tk.Button(self.root, text="Simpan", font=("Arial", 12), bg="#77dd77", fg="white", command=self.save_notes)
        save_button.pack(pady=5)

        load_button = tk.Button(self.root, text="Buka", font=("Arial", 12), bg="#77dd77", fg="white", command=self.load_notes)
        load_button.pack(pady=5)

    def save_notes(self):
        notes_content = self.text_area.get("1.0", tk.END).strip()
        if notes_content:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(notes_content)
                messagebox.showinfo("Success", "Catatan berhasil disimpan!")
        else:
            messagebox.showwarning("Warning", "Catatan kosong! Tidak ada yang disimpan.")

    def load_notes(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                notes_content = file.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, notes_content)
            messagebox.showinfo("Success", "Catatan berhasil dimuat!")

root = tk.Tk()
notes_app = Notes(root)
root.mainloop()
