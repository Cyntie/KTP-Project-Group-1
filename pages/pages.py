import tkinter as tk

from pages.production_questions_page import ProductionQuestionPage
from pages.cleaning_questions_page import CleaningQuestionPage
from pages.results_page import ResultsPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Hello World")
        self.geometry("500x500")
        
        self.state_mode = None
        self.pages = {}
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand = True)
                
        for PageClass in (StartPage, ProductionQuestionPage, CleaningQuestionPage, ResultsPage):
            page = PageClass(self.container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")
            
        self.show_page(StartPage)
        
    def show_page(self, page_class):
        page=self.pages[page_class]
        page.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, 
                 text="Are we running a production state or cleaning state?",
                 font=("Arial", 14)).pack(pady=10)

        # Production button
        tk.Button(self, text="Production",
                  font=("Arial", 14),
                  bg="#E0C2FF", fg="#0D001A",
                  command=self.set_production).pack(pady=5)

        # Cleaning button
        tk.Button(self, text="Cleaning",
                  font=("Arial", 14),
                  bg="#E0C2FF", fg="#0D001A",
                  command=self.set_cleaning).pack(pady=5)

    def set_production(self):
        self.controller.state_mode = "production"
        self.controller.show_page(ProductionQuestionPage)

    def set_cleaning(self):
        self.controller.state_mode = "cleaning"
        self.controller.show_page(CleaningQuestionPage)

