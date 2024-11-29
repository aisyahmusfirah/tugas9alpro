from Timer.timer import Timer
from Notes.notes import Notes
from Todolist.todolist import Todoist
from Calculator.calculator import Calculator

# Fungsi untuk setiap fitur
def open_timer():
    TimerApp()

def open_notes():
    NotesApp()

def open_todo_list():
    ToDoListApp()

def open_calculator():
    CalculatorApp()

# Membuat aplikasi utama
app = Tk()
app.title("Student Productivity Toolkit")
app.geometry("400x300")  # Ukuran jendela aplikasi

# Membuat menu navigasi
menu_bar = Menu(app)

# Menu "Features"
features_menu = Menu(menu_bar, tearoff=0)
features_menu.add_command(label="Timer", command=open_timer)
features_menu.add_command(label="Notes", command=open_notes)
features_menu.add_command(label="To-Do List", command=open_todo_list)
features_menu.add_command(label="Calculator", command=open_calculator)
menu_bar.add_cascade(label="Features", menu=features_menu)

# Menambahkan menu ke aplikasi
app.config(menu=menu_bar)

# Menjalankan aplikasi
app.mainloop()

