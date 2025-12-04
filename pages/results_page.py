import tkinter as tk

class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, 
                 text="Machine is clean/dirty",
                 font=("Arial", 14)).pack(pady=10)