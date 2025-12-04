import tkinter as tk
from tkinter import messagebox
from pages.results_page import ResultsPage

class CleaningQuestionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Enter current fouling rate in ... :", font=("Arial", 14)).pack(pady=10)
        self.curr_foul_rate_var = tk.StringVar()
        self.curr_foul_rate = tk.Entry(self, textvariable=self.curr_foul_rate_var, font=("Arial", 14))
        self.curr_foul_rate.pack(pady=5)

        tk.Label(self, text="Enter current pump capacity in ... :", font=("Arial", 14)).pack(pady=10)
        self.curr_pump_capacity_var = tk.StringVar()
        self.curr_pump_capacity = tk.Entry(self, textvariable=self.curr_pump_capacity_var, font=("Arial", 14))
        self.curr_pump_capacity.pack(pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).pack(pady=10)
    
    def save_values(self):
        try:
            value = float(self.curr_pump_capacity_var.get())
            self.controller.curr_pump_capacity = value
        except ValueError:
            messagebox.showerror("Invalid input for 'pump capacity'", "Please enter a number.")
            return
        try:
            value = float(self.curr_foul_rate_var.get())
            self.controller.curr_foul_rate = value
        except ValueError:
            messagebox.showerror("Invalid input for 'fouling rate'", "Please enter a number.")
            return
        self.controller.show_page(ResultsPage)