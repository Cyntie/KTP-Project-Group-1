import tkinter as tk
from tkinter import ttk, messagebox
from pages.results_page import ResultsPage

class HeatExchangerProductionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Heat Exchanger – Production Page", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

        #Product type
        tk.Label(self, text="Choose product type:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.product_type = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self, textvariable=self.product_type, state='readonly')
        self.product_dropdown['values'] = ("Skim milk", "Whole milk", "Cream")
        self.product_dropdown.current(0)
        self.product_dropdown.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        #Current run time
        tk.Label(self, text="Enter run time in hours:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Arial", 14))
        self.entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        #Current pump power
        tk.Label(self, text="Enter current pump power in kW:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_power_var = tk.StringVar()
        self.curr_pump_power = tk.Entry(self, textvariable=self.curr_pump_power_var, font=("Arial", 14))
        self.curr_pump_power.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        #Set pump power
        tk.Label(self, text="Enter set pump power in kW:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.set_pump_power_var = tk.StringVar()
        self.set_pump_power = tk.Entry(self, textvariable=self.set_pump_power_var, font=("Arial", 14))
        self.set_pump_power.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        #Current pump capacity
        tk.Label(self, text="Enter current pump capacity in L/h:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_capacity_var = tk.StringVar()
        self.curr_pump_capacity = tk.Entry(self, textvariable=self.curr_pump_capacity_var, font=("Arial", 14))
        self.curr_pump_capacity.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        #Set pump capacity
        tk.Label(self, text="Enter set pump capacity in L/h:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.set_pump_capacity_var = tk.StringVar()
        self.set_pump_capacity = tk.Entry(self, textvariable=self.set_pump_capacity_var, font=("Arial", 14))
        self.set_pump_capacity.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        #Water-in temperature
        tk.Label(self, text="Enter water-in temperature in degrees Celcius:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.temp_water_in_var = tk.StringVar()
        self.temp_water_in = tk.Entry(self, textvariable=self.temp_water_in_var, font=("Arial", 12))
        self.temp_water_in.grid(row=7, column=1, sticky="w", padx=5, pady=5)

        #Product-out temperature
        tk.Label(self, text="Enter product-out temperature in degrees Celcius:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.temp_product_out_var = tk.StringVar()
        self.temp_product_out = tk.Entry(self, textvariable=self.temp_product_out_var, font=("Arial", 12))
        self.temp_product_out.grid(row=8, column=1, sticky="w", padx=5, pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).grid(row=9, column=0, columnspan=2, pady=10)

    def save_values(self):
        self.controller.selected_product = self.product_type.get()
        #Run time
        try:
            value = float(self.entry_var.get())
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
        
        #Set pump capacity
        try:
            value = float(self.set_pump_power_var.get())
            self.controller.set_pump_power = value
        except ValueError:
            messagebox.showerror("Invalid input for 'set pump power'", "Please enter a number.")
            return
        
        #Current pump capacity
        try:
            value = float(self.curr_pump_capacity_var.get())
            self.controller.curr_pump_capacity = value
        except ValueError:
            messagebox.showerror("Invalid input for 'current pump capacity'", "Please enter a number.")
            return
        
        #Set pump capacity
        try:
            value = float(self.set_pump_capacity_var.get())
            self.controller.set_pump_capacity = value
        except ValueError:
            messagebox.showerror("Invalid input for 'set pump capacity'", "Please enter a number.")
            return
        
        #Water-in temperature
        try:
            value = float(self.temp_water_in_var.get())
            self.controller.temp_water_in = value
        except ValueError:
            messagebox.showerror("Invalid input for 'water temperature'", "Please enter a number.")
            return
        
        #Product-out temperature
        try:
            value = float(self.temp_product_out_var.get())
            self.controller.temp_product_out = value
        except ValueError:
            messagebox.showerror("Invalid input for 'product temperature'", "Please enter a number.")
            return
        self.controller.show_page(ResultsPage)