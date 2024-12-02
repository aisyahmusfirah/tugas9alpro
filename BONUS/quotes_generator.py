import tkinter as tk
import random

class MotivationalQuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motivational Quote Generator")
        self.root.geometry("400x200")
        self.root.config(bg="#FEE2E2")

        self.quotes = [
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

        self.quote_label = tk.Label(self.root, text="", font=("Times New Roman", 16, "italic"), fg="#000000", bg="#FEE2E2", wraplength=350)
        self.quote_label.pack(pady=20)

        self.quote_button = tk.Button(self.root, text="Generate Quote", font=("Times New Roman", 12), bg="#FFB3C1", fg="black", command=self.show_quote, relief="solid", bd=1)
        self.quote_button.pack(pady=10)

    def show_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=quote)

if __name__ == "__main__":
    root = tk.Tk()
    app = MotivationalQuoteApp(root)
    root.mainloop()
