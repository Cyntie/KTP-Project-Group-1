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

        #Pump capacity t₁
        tk.Label(self, text="Enter pump capacity at t₁:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.pump_capacity_t1_var = tk.StringVar()
        self.pump_capacity_t1 = tk.Entry(self, textvariable=self.pump_capacity_t1_var, font=("Arial", 12))
        self.pump_capacity_t1.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="L/h", font=("Arial", 12)).grid(row=2, column=2, sticky="w", padx=5, pady=5)
        
        #Pump capacity t₂
        tk.Label(self, text="Enter pump capacity at t₂:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.pump_capacity_t2_var = tk.StringVar()
        self.pump_capacity_t2 = tk.Entry(self, textvariable=self.pump_capacity_t2_var, font=("Arial", 12))
        self.pump_capacity_t2.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="L/h", font=("Arial", 12)).grid(row=3, column=2, sticky="w", padx=5, pady=5)

        #Air-in temperature t₁
        tk.Label(self, text="Enter air-in temperature at t₁:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.temp_air_in_t1_var = tk.StringVar()
        self.temp_air_in_t1 = tk.Entry(self, textvariable=self.temp_air_in_t1_var, font=("Arial", 12))
        self.temp_air_in_t1.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=4, column=2, sticky="w", padx=5, pady=5)

        #Product-out temperature t₁
        tk.Label(self, text="Enter product-out temperature at t₁:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.temp_product_out_t1_var = tk.StringVar()
        self.temp_product_out_t1 = tk.Entry(self, textvariable=self.temp_product_out_t1_var, font=("Arial", 12))
        self.temp_product_out_t1.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=5, column=2, sticky="w", padx=5, pady=5)

        #Air-in temperature t₂
        tk.Label(self, text="Enter air-in temperature at t₂:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.temp_air_in_t2_var = tk.StringVar()
        self.temp_air_in_t2 = tk.Entry(self, textvariable=self.temp_air_in_t2_var, font=("Arial", 12))
        self.temp_air_in_t2.grid(row=6, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=6, column=2, sticky="w", padx=5, pady=5)

        #Product-out temperature t₂
        tk.Label(self, text="Enter product-out temperature at t₂:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)
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
        
        #Pump capacity t₁
        try:
            value = float(self.pump_capacity_t1_var.get())
            self.controller.pump_capacity_t1 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'pump capacity at t₁'", "Please enter a number.")
            return
        
        #Pump capacity t₂
        try:
            value = float(self.pump_capacity_t2_var.get())
            self.controller.pump_capacity_t2 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'pump capacity at t₂'", "Please enter a number.")
            return
        
        #Air-in temperature t₁
        try:
            value = float(self.temp_air_in_t1_var.get())
            self.controller.temp_air_in_t1 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'air temperature at t₁'", "Please enter a number.")
            return
        
        #Product-out temperature t₁
        try:
            value = float(self.temp_product_out_t1_var.get())
            self.controller.temp_product_out_t1 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'product temperature at t₁'", "Please enter a number.")
            return
        
        # Check that air-in temperature is always higher than product-out temperature
        if self.controller.temp_air_in_t1 < self.controller.temp_product_out_t1:
            messagebox.showerror(
                "Invalid temperatures",
                "Air-in temperature must be higher than product-out temperature at t₁."
            )
            return

        #Air-in temperature t₂
        try:
            value = float(self.temp_air_in_t2_var.get())
            self.controller.temp_air_in_t2 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'air temperature at t₂'", "Please enter a number.")
            return
        
        #Product-out temperature t₂
        try:
            value = float(self.temp_product_out_t2_var.get())
            self.controller.temp_product_out_t2 = value
        except ValueError:
            messagebox.showerror("Invalid input for 'product temperature at t₂'", "Please enter a number.")
            return

        # Check that air-in temperature is always higher than product-out temperature        
        if self.controller.temp_air_in_t2 < self.controller.temp_product_out_t2:
            messagebox.showerror(
                "Invalid temperatures",
                "Air-in temperature must be higher than product-out temperature at t₂."
            )
            return

        self.controller.show_page(ResultsPage)

