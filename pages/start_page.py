import tkinter as tk
from tkinter import ttk

from pages.he_production_page import HeatExchangerProductionPage
from pages.he_cleaning_page import HeatExchangerCleaningPage
from pages.ev_production_page import EvaporatorProductionPage
from pages.ev_cleaning_page import EvaporatorCleaningPage
from pages.dr_production_page import DryerProductionPage
from pages.dr_cleaning_page import DryerCleaningPage
from pages.me_production_page import MembranesProductionPage
from pages.me_cleaning_page import MembranesCleaningPage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="Select Machine Type:", font=("Arial", 14)).pack(pady=10)
        self.machine_var = tk.StringVar()
        machine_dropdown = ttk.Combobox(self, textvariable=self.machine_var)
        machine_dropdown['values'] = ("Heat Exchanger", "Evaporator", "Dryer", "Membranes")
        machine_dropdown.pack(pady=5)

        tk.Label(self, text="Select Machine State:", font=("Arial", 14)).pack(pady=10)
        self.state_var = tk.StringVar()
        state_dropdown = ttk.Combobox(self, textvariable=self.state_var)
        state_dropdown['values'] = ("Production", "Cleaning")
        state_dropdown.pack(pady=5)

        tk.Button(self, text="Next", font=("Arial", 14), bg="#E0C2FF", fg="#0D001A",
                  command=self.go_to_next_page).pack(pady=20)
        
    def go_to_next_page(self):
        self.controller.machine_type = self.machine_var.get()
        self.controller.state_mode = self.state_var.get()

        if self.controller.machine_type == "Heat Exchanger" and self.controller.state_mode == "Production":
            self.controller.show_page(HeatExchangerProductionPage)
        elif self.controller.machine_type == "Heat Exchanger" and self.controller.state_mode == "Cleaning":
            self.controller.show_page(HeatExchangerCleaningPage)
        elif self.controller.machine_type == "Evaporator" and self.controller.state_mode == "Production":
            self.controller.show_page(EvaporatorProductionPage)
        elif self.controller.machine_type == "Evaporator" and self.controller.state_mode == "Cleaning":
            self.controller.show_page(EvaporatorCleaningPage)
        elif self.controller.machine_type == "Dryer" and self.controller.state_mode == "Production":
            self.controller.show_page(DryerProductionPage)
        elif self.controller.machine_type == "Dryer" and self.controller.state_mode == "Cleaning":
            self.controller.show_page(DryerCleaningPage)
        elif self.controller.machine_type == "Membranes" and self.controller.state_mode == "Production":
            self.controller.show_page(MembranesProductionPage)
        elif self.controller.machine_type == "Membranes" and self.controller.state_mode == "Cleaning":
            self.controller.show_page(MembranesCleaningPage)
        else:
            tk.messagebox.showerror("Selection Error", "Page not implemented yet.")

