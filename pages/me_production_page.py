import tkinter as tk
from tkinter import messagebox, ttk
from pages.results_page import ResultsPage

class MembranesProductionPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Membranes – Production Page", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

        #Membrane type
        tk.Label(self, text="Choose membrane type:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.membrane_type = tk.StringVar()
        self.membrane_dropdown = ttk.Combobox(self, textvariable=self.membrane_type, state='readonly')
        self.membrane_dropdown['values'] = ("Micro Filtration", "Ultra Filtration", "Nano Filtration", "Reversed Osmosis")
        self.membrane_dropdown.current(0)
        self.membrane_dropdown.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        #Current TMP
        tk.Label(self, text="Enter current TMP:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.curr_tmp_var = tk.StringVar()
        self.curr_tmp = tk.Entry(self, textvariable=self.curr_tmp_var, font=("Arial", 12))
        self.curr_tmp.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        tk.Label(self, text="mbar", font=("Arial", 12)).grid(row=2, column=2, sticky="w", padx=5, pady=5)

        tk.Button(self, text="Submit", font=("Arial", 14), command=self.save_values).grid(row=3, column=0, columnspan=2, pady=10)

    def save_values(self):
        self.controller.membrane = self.membrane_type.get()
        
        #Current TMP
        try:
            value = float(self.curr_tmp_var.get())
            self.controller.curr_tmp = value
        except ValueError:
            messagebox.showerror("Invalid input for 'Current TMP'", "Please enter a number.")
            return
        
        self.controller.show_page(ResultsPage)