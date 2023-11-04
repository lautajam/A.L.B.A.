import tkinter as tk
from controller.websearch import web_search

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("A.L.B.A.")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="¡Hola, Tkinter!")
        self.label.pack()

        self.button = tk.Button(self.root, text="Haz clic", command=self.button_click)
        self.button.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

    def button_click(self):
        print("¡Botón presionado!")
        web_search()