import tkinter as tk
from tkinter import messagebox, ttk
from pages.results_page import ResultsPage

class HeatExchangerCleaningPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Heat Exchanger – Cleaning Page", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

        #Current pump power
        tk.Label(self, text="Enter current pump power:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_power_var = tk.StringVar()
        self.curr_pump_power = tk.Entry(self, textvariable=self.curr_pump_power_var, font=("Arial", 12))
        self.curr_pump_power.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="kW", font=("Arial", 12)).grid(row=1, column=2, sticky="w", padx=5, pady=5)

        #Water-in temperature
        tk.Label(self, text="Enter water-in temperature:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.temp_water_in_var = tk.StringVar()
        self.temp_water_in = tk.Entry(self, textvariable=self.temp_water_in_var, font=("Arial", 12))
        self.temp_water_in.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=2, column=2, sticky="w", padx=5, pady=5)

        #Product-out temperature
        tk.Label(self, text="Enter product-out temperature:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.temp_product_out_var = tk.StringVar()
        self.temp_product_out = tk.Entry(self, textvariable=self.temp_product_out_var, font=("Arial", 12))
        self.temp_product_out.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=3, column=2, sticky="w", padx=5, pady=5)

        #Pressure start
        tk.Label(self, text="Enter pressure at the start:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.start_pressure_var = tk.StringVar()
        self.start_pressure = tk.Entry(self, textvariable=self.start_pressure_var, font=("Arial", 12))
        self.start_pressure.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="bar", font=("Arial", 12)).grid(row=4, column=2, sticky="w", padx=5, pady=5)

        #Pressure end
        tk.Label(self, text="Enter pressure at the end:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.end_pressure_var = tk.StringVar()
        self.end_pressure = tk.Entry(self, textvariable=self.end_pressure_var, font=("Arial", 12))
        self.end_pressure.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="bar", font=("Arial", 12)).grid(row=5, column=2, sticky="w", padx=5, pady=5)

        #75°C time
        tk.Label(self, text="Enter 75°C time in minutes:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.time_at_75_var = tk.StringVar()
        self.time_at_75 = tk.Entry(self, textvariable=self.time_at_75_var, font=("Arial", 12))
        self.time_at_75.grid(row=6, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="min", font=("Arial", 12)).grid(row=6, column=2, sticky="w", padx=5, pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).grid(row=7, column=0, columnspan=2, pady=10)
    
    def save_values(self):
        #Current pump power
        try:
            value = float(self.curr_pump_power_var.get())
            self.controller.curr_pump_power = value
        except ValueError:
            messagebox.showerror("Invalid input for 'current pump power'", "Please enter a number.")
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

        # Check that water-in temperature is always higher than product-out temperature        
        if self.controller.temp_water_in < self.controller.temp_product_out:
            messagebox.showerror(
                "Invalid temperatures",
                "Water-in temperature must be higher than product-out temperature."
            )
            return
        
        #Pressure start
        try:
            value = float(self.start_pressure_var.get())
            self.controller.start_pressure = value
        except ValueError:
            messagebox.showerror("Invalid input for 'start pressure'", "Please enter a number.")
            return
        
        #Pressure end
        try:
            value = float(self.end_pressure_var.get())
            self.controller.end_pressure = value
        except ValueError:
            messagebox.showerror("Invalid input for 'end pressure'", "Please enter a number.")
            return
        
        # Check that end pressure temperature is always higher than start pressure        
        if self.controller.end_pressure < self.controller.start_pressure:
            messagebox.showerror(
                "Invalid pressures",
                "End pressure temperature must be higher than start pressure."
            )
            return
        
        #75°C time
        try:
            value = float(self.time_at_75_var.get())
            self.controller.time_at_75 = value
        except ValueError:
            messagebox.showerror("Invalid input for '75°C time'", "Please enter a number.")
            return
        self.controller.show_page(ResultsPage)