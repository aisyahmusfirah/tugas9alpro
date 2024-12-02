import tkinter as tk
from Timer.timer import Timer
from Notes.notes import Notes
from Todolist.todolist import Todolist
from Calculator.calculator import Calculator
from BONUS.quotes_generator import MotivationalQuoteApp

class StudentProductivityToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Productivity Toolkit")
        self.root.geometry("400x400")
        self.root.config(bg="#f7f7f7")

        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root,
            text="Student Productivity Toolkit",
            font=("Arial", 18, "bold"),
            bg="#f7f7f7",
            fg="#333"
        ).pack(pady=20)

        self.create_button("Timer", self.open_timer)
        self.create_button("Notes", self.open_notes)
        self.create_button("To-Do List", self.open_todo_list)
        self.create_button("Calculator", self.open_calculator)
        self.create_button("Motivational Quotes", self.open_bonus)

    def create_button(self, label, command):
        tk.Button(
            self.root,
            text=label,
            font=("Arial", 14),
            bg="#FFB6C1",
            fg="black",
            width=20,
            command=command
        ).pack(pady=10)

    def open_timer(self):
        self.switch_to_feature(Timer)

    def open_notes(self):
        self.switch_to_feature(Notes)

    def open_todo_list(self):
        self.switch_to_feature(Todolist)

    def open_calculator(self):
        self.switch_to_feature(Calculator)

    def open_bonus(self):
        self.switch_to_feature(MotivationalQuoteApp)

    def switch_to_feature(self, feature_class):
        """Switch to a specific feature by initializing its class."""
        for widget in self.root.winfo_children():
            widget.destroy() 
        feature_class(self.root)  

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentProductivityToolkit(root)
    root.mainloop()
