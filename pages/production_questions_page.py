import tkinter as tk
from tkinter import ttk, messagebox
from pages.results_page import ResultsPage

class ProductionQuestionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
    
        tk.Label(self, text="Choose product type:", font=("Arial", 14)).pack(pady=5)
        self.product_type = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self, textvariable=self.product_type, state='readonly')
        self.product_dropdown['values'] = ("Skim milk", "High fat product")
        self.product_dropdown.current(0)
        self.product_dropdown.pack(pady=5)

        tk.Label(self, text="Enter run time in hours:", font=("Arial", 14)).pack(pady=10)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Arial", 14))
        self.entry.pack(pady=5)

        tk.Label(self, text="Enter water-in temperature in degrees Celcius:", font=("Arial", 14)).pack(pady=10)
        self.temp_water_in_var = tk.StringVar()
        self.temp_water_in = tk.Entry(self, textvariable=self.temp_water_in_var, font=("Arial", 14))
        self.temp_water_in.pack(pady=5)

        tk.Label(self, text="Enter product-out temperature in degrees Celcius:", font=("Arial", 14)).pack(pady=10)
        self.temp_product_out_var = tk.StringVar()
        self.temp_product_out = tk.Entry(self, textvariable=self.temp_product_out_var, font=("Arial", 14))
        self.temp_product_out.pack(pady=5)

        tk.Label(self, text="Enter current pump capacity in ... :", font=("Arial", 14)).pack(pady=10)
        self.curr_pump_capacity_var = tk.StringVar()
        self.curr_pump_capacity = tk.Entry(self, textvariable=self.curr_pump_capacity_var, font=("Arial", 14))
        self.curr_pump_capacity.pack(pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).pack(pady=10)

    def save_values(self):
        self.controller.selected_product = self.product_type.get()
        try:
            value = float(self.entry_var.get())
            self.controller.run_time = value
        except ValueError:
            messagebox.showerror("Invalid input for 'run time'", "Please enter a number.")
            return
        try:
            value = float(self.temp_water_in_var.get())
            self.controller.temp_water_in = value
        except ValueError:
            messagebox.showerror("Invalid input for 'water temperature'", "Please enter a number.")
            return
        try:
            value = float(self.temp_product_out_var.get())
            self.controller.temp_product_out = value
        except ValueError:
            messagebox.showerror("Invalid input for 'product temperature'", "Please enter a number.")
            return
        try:
            value = float(self.curr_pump_capacity_var.get())
            self.controller.curr_pump_capacity = value
        except ValueError:
            messagebox.showerror("Invalid input for 'pump capacity'", "Please enter a number.")
            return
        self.controller.show_page(ResultsPage)