import tkinter as tk
from . import ConfigScreen as cScreen
from controller.websearch import web_search
from resources.text import MainScreenTxt as ms_txt

class main_screen:
    def __init__(self, root):
        self.root = root
        self.root.title("A.L.B.A.")
        self.root.geometry("600x380")

        self.welcome_txt = ms_txt.welcome_txt
        self.welcomelbl  = tk.Label(self.root, 
                                    text = self.welcome_txt,
                                    font =("Arial", 15),
                                    foreground = "black",
                                    padx = 10, pady = 10,
                                   )
        self.welcomelbl.pack()

        self.presentation_txt = ms_txt.presentation_txt
        self.presentation_lbl = tk.Label(self.root, 
                                         text = self.presentation_txt, 
                                         wraplength = 500,
                                         font = ("Arial", 12),
                                         padx =10, pady = 10,
                                        ) 
        self.presentation_lbl.pack()
         
        self.search_txt = ms_txt.search_btn_txt
        self.search_btn = tk.Button(self.root, 
                                    text = self.search_txt,
                                    font = ("Arial", 10),
                                    command = self.init_web_search,
                                    )
        self.search_btn.pack(pady = 5)

        self.configurations_txt = ms_txt.configutarion_btn_txt
        self.configurations_btn = tk.Button(self.root,  
                                            text = self.configurations_txt, 
                                            font = ("Arial", 10),
                                            command = self.configuration_screen,
                                            )
        self.configurations_btn.pack(pady = 5)

        self.exit_txt = ms_txt.exit_btn_txt
        self.exit_btn = tk.Button(self.root,
                                  text = self.exit_txt,
                                  font = ("Arial", 10),
                                  command = self.exit_app,
                                  )
        self.exit_btn.pack(pady = 5)

    # Methods
    """
    This function initializes the web search process, that is, 
    it asks the user for a query and opens the first result in Brave browser
    """
    def init_web_search(self):
        web_search()

    """
    This function opens the configuration screen of the app
    """
    def configuration_screen(self):
        cScreen.ConfigScreen(self.root)

    """
    This function closes the app
    """
    def exit_app(self):
        print("Exiting...")
        self.root.destroy()
