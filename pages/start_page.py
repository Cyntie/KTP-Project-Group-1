import tkinter as tk
from tkinter import ttk, messagebox

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

        outer = tk.Frame(self)
        outer.pack(expand=True)

        title = tk.Label(
            outer,
            text="Assessing Machine Cleanliness",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=(0, 20))

        card = tk.Frame(
            outer,
            padx=30,
            pady=25,
            bd=1,
            relief="solid"
        )
        card.pack()

        self.machine_var = tk.StringVar(value="Select machine…")
        self.state_var = tk.StringVar(value="Select state…")

        tk.Label(card, text="Machine Type", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="n", pady=(0, 6))
        self.machine_dropdown = ttk.Combobox(
            card,
            textvariable=self.machine_var,
            state="readonly",
            width=26,
            values=("Heat Exchanger", "Evaporator", "Dryer", "Membranes")
        )
        self.machine_dropdown.grid(row=1, column=0, sticky="n", pady=(0, 14))

        tk.Label(card, text="Machine State", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="n", pady=(0, 6))
        self.state_dropdown = ttk.Combobox(
            card,
            textvariable=self.state_var,
            state="readonly",
            width=26,
            values=("Production", "Cleaning")
        )
        self.state_dropdown.grid(row=3, column=0, sticky="n", pady=(0, 18))

        card.grid_columnconfigure(0, weight=1)

        next_btn = tk.Button(
            card,
            text="Next →",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#43A047",
            activeforeground="white",
            padx=18,
            pady=6,
            command=self.go_to_next_page
        )
        next_btn.grid(row=4, column=0, pady=(6, 0))

        self.bind_all("<Return>", lambda e: self.go_to_next_page())

        self._routes = {
            ("Heat Exchanger", "Production"): HeatExchangerProductionPage,
            ("Heat Exchanger", "Cleaning"): HeatExchangerCleaningPage,
            ("Evaporator", "Production"): EvaporatorProductionPage,
            ("Evaporator", "Cleaning"): EvaporatorCleaningPage,
            ("Dryer", "Production"): DryerProductionPage,
            ("Dryer", "Cleaning"): DryerCleaningPage,
            ("Membranes", "Production"): MembranesProductionPage,
            ("Membranes", "Cleaning"): MembranesCleaningPage,
        }

    def go_to_next_page(self):
        machine = self.machine_var.get()
        state = self.state_var.get()

        if machine == "Select machine…" or not machine:
            messagebox.showerror("Selection Error", "Please select a machine type.")
            return
        if state == "Select state…" or not state:
            messagebox.showerror("Selection Error", "Please select a machine state.")
            return

        self.controller.machine_type = machine
        self.controller.state_mode = state

        page_class = self._routes.get((machine, state))
        if page_class is None:
            messagebox.showerror("Selection Error", "Page not implemented yet.")
            return

        self.controller.show_page(page_class)
