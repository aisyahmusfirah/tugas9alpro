import tkinter as tk
import random

quotes = [
    "Keberhasilan tidak datang kepada mereka yang menunggu, tetapi kepada mereka yang berjuang.",
    "Jangan menyerah, karena kesuksesan bisa datang pada detik terakhir.",
    "Setiap langkah kecil membawa kita lebih dekat ke tujuan.",
    "Percaya pada dirimu sendiri dan semua yang kamu lakukan.",
    "Hidupmu adalah hasil dari pilihan-pilihan yang kamu buat.",
    "Keberhasilan bukanlah akhir, kegagalan bukanlah hal yang fatal: yang penting adalah keberanian untuk melanjutkan. — Winston Churchill",
    "Jangan pernah menyerah, karena hanya dengan terus berusaha kita akan menemukan kekuatan dalam diri kita.",
    "Setiap hari adalah kesempatan baru untuk menjadi lebih baik dari sebelumnya.",
    "Pikiran kita adalah alat yang sangat kuat. Gunakanlah untuk meraih impianmu.",
    "Keberanian untuk mencoba adalah langkah pertama menuju kesuksesan."
]

# Fungsi untuk menampilkan kutipan secara acak
def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

# Membuat jendela utama
root = tk.Tk()
root.title("Motivational Quote Generator")
root.geometry("400x200")
root.config(bg="#FEE2E2")

# Label untuk menampilkan kutipan
quote_label = tk.Label(root, text="", font=("Times New Roman", 16, "italic"), fg="#000000", bg="#FEE2E2", wraplength=350)
quote_label.pack(pady=20)

# Tombol untuk menampilkan kutipan baru
quote_button = tk.Button(root, text="Generate Quote", font=("Times New Roman", 12), bg="#FFB3C1", fg="black", command=show_quote, relief="solid", bd=1)
quote_button.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
