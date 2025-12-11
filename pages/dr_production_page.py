import tkinter as tk
from tkinter import messagebox
from pages.results_page import ResultsPage

class DryerProductionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Dryer – Production Page", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

        #Current pump power
        tk.Label(self, text="Enter current pump power:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_power_var = tk.StringVar()
        self.curr_pump_power = tk.Entry(self, textvariable=self.curr_pump_power_var, font=("Arial", 12))
        self.curr_pump_power.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="kW", font=("Arial", 12)).grid(row=1, column=2, sticky="w", padx=5, pady=5)

        #Pump capacity t1
        tk.Label(self, text="Enter pump capacity at t1:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.pump_capacity_t1_var = tk.StringVar()
        self.pump_capacity_t1 = tk.Entry(self, textvariable=self.pump_capacity_t1_var, font=("Arial", 12))
        self.pump_capacity_t1.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="L/h", font=("Arial", 12)).grid(row=2, column=2, sticky="w", padx=5, pady=5)
        
        #Pump capacity t2
        tk.Label(self, text="Enter pump capacity at t2:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.pump_capacity_t2_var = tk.StringVar()
        self.pump_capacity_t2 = tk.Entry(self, textvariable=self.pump_capacity_t2_var, font=("Arial", 12))
        self.pump_capacity_t2.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="L/h", font=("Arial", 12)).grid(row=3, column=2, sticky="w", padx=5, pady=5)

        #Air-in temperature t1
        tk.Label(self, text="Enter air-in temperature at t1:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.temp_air_in_t1_var = tk.StringVar()
        self.temp_air_in_t1 = tk.Entry(self, textvariable=self.temp_air_in_t1_var, font=("Arial", 12))
        self.temp_air_in_t1.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=4, column=2, sticky="w", padx=5, pady=5)

        #Product-out temperature t1
        tk.Label(self, text="Enter product-out temperature at t1:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.temp_product_out_t1_var = tk.StringVar()
        self.temp_product_out_t1 = tk.Entry(self, textvariable=self.temp_product_out_t1_var, font=("Arial", 12))
        self.temp_product_out_t1.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=5, column=2, sticky="w", padx=5, pady=5)

        #Air-in temperature t2
        tk.Label(self, text="Enter air-in temperature at t2:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.temp_air_in_t2_var = tk.StringVar()
        self.temp_air_in_t2 = tk.Entry(self, textvariable=self.temp_air_in_t2_var, font=("Arial", 12))
        self.temp_air_in_t2.grid(row=6, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=6, column=2, sticky="w", padx=5, pady=5)

        #Product-out temperature t2
        tk.Label(self, text="Enter product-out temperature at t2:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.temp_product_out_t2_var = tk.StringVar()
        self.temp_product_out_t2 = tk.Entry(self, textvariable=self.temp_product_out_t2_var, font=("Arial", 12))
        self.temp_product_out_t2.grid(row=7, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=7, column=2, sticky="w", padx=5, pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).grid(row=8, column=0, columnspan=2, pady=10)

    def save_values(self):
        
        #Current pump power
        try:
            value = float(self.curr_pump_power_var.get())
            self.controller.curr_pump_power = value
        except ValueError:
            messagebox.showerror("Invalid input for 'current pump power'", "Please enter a number.")
            return
        
        #Pump capacity t1
        try:
            value = float(self.pump_capacity_t1_var.get())
            self.controller.pump_capacity_t1 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'pump capacity at t1'", "Please enter a number.")
            return
        
        #Pump capacity t2
        try:
            value = float(self.pump_capacity_t2_var.get())
            self.controller.pump_capacity_t2 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'pump capacity at t2'", "Please enter a number.")
            return
        
        #Air-in temperature t1
        try:
            value = float(self.temp_air_in_t1_var.get())
            self.controller.temp_air_in_t1 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'air temperature at t1'", "Please enter a number.")
            return
        
        #Product-out temperature t1
        try:
            value = float(self.temp_product_out_t1_var.get())
            self.controller.temp_product_out_t1 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'product temperature at t1'", "Please enter a number.")
            return
        
        #Air-in temperature t2
        try:
            value = float(self.temp_air_in_t2_var.get())
            self.controller.temp_air_in_t2 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'air temperature at t2'", "Please enter a number.")
            return
        
        #Product-out temperature t2
        try:
            value = float(self.temp_product_out_t2_var.get())
            self.controller.temp_product_out_t2 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'product temperature at t2'", "Please enter a number.")
            return

        self.controller.show_page(ResultsPage)

