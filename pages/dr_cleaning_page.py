import tkinter as tk
from tkinter import messagebox, ttk
from pages.results_page import ResultsPage

class DryerCleaningPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Dryer – Cleaning Page", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

        #Cycle type
        tk.Label(self, text="Choose cycle type:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.cycle_type = tk.StringVar()
        self.cycle_dropdown = ttk.Combobox(self, textvariable=self.cycle_type, state='readonly')
        self.cycle_dropdown['values'] = ("Wet", "Dry")
        self.cycle_dropdown.current(0)
        self.cycle_dropdown.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        #Current run time
        tk.Label(self, text="Enter cleaning time:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.run_time_var = tk.StringVar()
        self.run_time = tk.Entry(self, textvariable=self.run_time_var, font=("Arial", 12))
        self.run_time.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="h", font=("Arial", 12)).grid(row=2, column=2, sticky="w", padx=5, pady=5)

        #Current pump power
        tk.Label(self, text="Enter current pump power:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_power_var = tk.StringVar()
        self.curr_pump_power = tk.Entry(self, textvariable=self.curr_pump_power_var, font=("Arial", 12))
        self.curr_pump_power.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="kW", font=("Arial", 12)).grid(row=3, column=2, sticky="w", padx=5, pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).grid(row=4, column=0, columnspan=2, pady=10)
    
    def save_values(self):
        self.controller.cycle = self.cycle_type.get()

        #Run time
        try:
            value = float(self.run_time_var.get())
            self.controller.run_time = value
        except ValueError:
            messagebox.showerror("Invalid input for 'run time'", "Please enter a number.")
            return
        
        #Current pump power
        try:
            value = float(self.curr_pump_power_var.get())
            self.controller.curr_pump_power = value
        except ValueError:
            messagebox.showerror("Invalid input for 'current pump power'", "Please enter a number.")
            return
        
        self.controller.show_page(ResultsPage)