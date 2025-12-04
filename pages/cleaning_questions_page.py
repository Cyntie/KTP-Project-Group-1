import tkinter as tk

class CleaningQuestionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, 
                 text="Cleaning state",
                 font=("Arial", 14)).pack(pady=10)