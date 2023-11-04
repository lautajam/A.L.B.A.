import tkinter as tk

class ConfigScreen:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Pantalla de Configuración")
        self.root.geometry("600x380")

        # Agregar widgets y lógica para la pantalla de configuraciones aquí
        self.label = tk.Label(self.root, text="Configuraciones")
        self.label.pack()

        # Agregar el mainloop para esta ventana
        self.root.mainloop()