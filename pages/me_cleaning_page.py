import tkinter as tk
from tkinter import messagebox
from pages.results_page import ResultsPage

class MembranesCleaningPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Membranes – Cleaning", font=("Arial", 14)).pack(pady=20)