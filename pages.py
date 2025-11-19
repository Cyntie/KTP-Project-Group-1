import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Hello World")
        self.geometry("500x500")
        
        self.pages = {}
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand = True)
                
        for PageClass in (StartPage,):
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
        
        tk.Label(self, text="Hello, World!",
                 font=("Arial", 14)).pack(pady=20)
        
        tk.Button(self, text="Begin",
                  font=("Arial", 16),
                  bg = "#E0C2FF", fg="#0D001A").pack(pady=10)