import tkinter as tk

from pages.start_page import StartPage

from pages.he_production_page import HeatExchangerProductionPage
from pages.he_cleaning_page import HeatExchangerCleaningPage
from pages.ev_production_page import EvaporatorProductionPage
from pages.ev_cleaning_page import EvaporatorCleaningPage
from pages.dr_production_page import DryerProductionPage
from pages.dr_cleaning_page import DryerCleaningPage
from pages.me_production_page import MembranesProductionPage
from pages.me_cleaning_page import MembranesCleaningPage
from pages.results_page import ResultsPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Assessing Machine Cleanliness")
        self.geometry("700x700")
        
        self.state_mode = None
        self.machine_type = None
        self.pages = {}
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
                
        for PageClass in (StartPage, 
                          HeatExchangerProductionPage, HeatExchangerCleaningPage, 
                          EvaporatorProductionPage, EvaporatorCleaningPage, 
                          DryerProductionPage, DryerCleaningPage, 
                          MembranesProductionPage, MembranesCleaningPage, 
                          ResultsPage):
            page = PageClass(self.container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")
            
        self.show_page(StartPage)
        
    def show_page(self, page_class):
        page = self.pages[page_class]
        if hasattr(page, "on_show"):
            page.on_show()
        page.tkraise()