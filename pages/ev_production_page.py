import tkinter as tk
from tkinter import messagebox, ttk
from pages.results_page import ResultsPage

class EvaporatorProductionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Evaporator – Production Page", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

        #Fat content
        tk.Label(self, text="Fat content of product:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.fat_content = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self, textvariable=self.fat_content, state='readonly')
        self.product_dropdown['values'] = ("0.5%", "4%", "8%")
        self.product_dropdown.current(0)
        self.product_dropdown.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        #Protein content
        tk.Label(self, text="Protein content of product:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.protein_content = tk.StringVar()
        self.product_dropdown = ttk.Combobox(self, textvariable=self.protein_content, state='readonly')
        self.product_dropdown['values'] = ("0.5%", "4%")
        self.product_dropdown.current(0)
        self.product_dropdown.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        #Current run time
        tk.Label(self, text="Enter run time:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.run_time_var = tk.StringVar()
        self.run_time = tk.Entry(self, textvariable=self.run_time_var, font=("Arial", 12))
        self.run_time.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="h", font=("Arial", 12)).grid(row=3, column=2, sticky="w", padx=5, pady=5)

        #Current pump power
        tk.Label(self, text="Enter current pump power:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_power_var = tk.StringVar()
        self.curr_pump_power = tk.Entry(self, textvariable=self.curr_pump_power_var, font=("Arial", 12))
        self.curr_pump_power.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="kW", font=("Arial", 12)).grid(row=4, column=2, sticky="w", padx=5, pady=5)

        #Current pump capacity
        tk.Label(self, text="Enter current pump capacity:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.curr_pump_capacity_var = tk.StringVar()
        self.curr_pump_capacity = tk.Entry(self, textvariable=self.curr_pump_capacity_var, font=("Arial", 12))
        self.curr_pump_capacity.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="L/h", font=("Arial", 12)).grid(row=5, column=2, sticky="w", padx=5, pady=5)

        #Water-in temperature
        tk.Label(self, text="Enter water-in temperature:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.temp_water_in_var = tk.StringVar()
        self.temp_water_in = tk.Entry(self, textvariable=self.temp_water_in_var, font=("Arial", 12))
        self.temp_water_in.grid(row=6, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=6, column=2, sticky="w", padx=5, pady=5)

        #Product-out temperature
        tk.Label(self, text="Enter product-out temperature:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.temp_product_out_var = tk.StringVar()
        self.temp_product_out = tk.Entry(self, textvariable=self.temp_product_out_var, font=("Arial", 12))
        self.temp_product_out.grid(row=7, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="°C", font=("Arial", 12)).grid(row=7, column=2, sticky="w", padx=5, pady=5)

        #Current density
        tk.Label(self, text="Enter current product density:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.curr_density_var = tk.StringVar()
        self.curr_density = tk.Entry(self, textvariable=self.curr_density_var, font=("Arial", 12))
        self.curr_density.grid(row=8, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="kg/m³", font=("Arial", 12)).grid(row=8, column=2, sticky="w", padx=5, pady=5)

        #Maximum density
        tk.Label(self, text="Enter maximum product density:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=5, pady=5)
        self.max_density_var = tk.StringVar()
        self.max_density = tk.Entry(self, textvariable=self.max_density_var, font=("Arial", 12))
        self.max_density.grid(row=9, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="kg/m³", font=("Arial", 12)).grid(row=9, column=2, sticky="w", padx=5, pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).grid(row=10, column=0, columnspan=2, pady=10)

    def save_values(self):
        self.controller.fat_content = self.fat_content.get()
        self.controller.protein_content = self.protein_content.get()

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
        
        #Current pump capacity
        try:
            value = float(self.curr_pump_capacity_var.get())
            self.controller.curr_pump_capacity = value
        except ValueError:
            messagebox.showerror("Invalid input for 'current pump capacity'", "Please enter a number.")
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

        #Current density
        try:
            value = float(self.curr_density_var.get())
            self.controller.curr_density = value
        except ValueError:
            messagebox.showerror("Invalid input for 'current density'", "Please enter a number.")
            return
        
        #Maximum density
        try:
            value = float(self.max_density_var.get())
            self.controller.max_density = value
        except ValueError:
            messagebox.showerror("Invalid input for 'maximum density'", "Please enter a number.")
            return

        self.controller.show_page(ResultsPage)