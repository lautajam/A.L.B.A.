import tkinter as tk
from tkinter import ttk

def onClick():
    print("Escuchando")

#Creo la ventana y la hago no modificable en tamaño
root = tk.Tk()
root.resizable(False, False)

# Estilos
style = ttk.Style()
style.configure("MyStyle.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style.configure("MyStyle.TLabel", font=("Arial", 14), padding=10, foreground="black")
root.title("A.U.R.A.")
root.geometry("600x200")

label = ttk.Label(root, text="Toca el botón para empezar la búsqueda y lectura por voz", style="MyStyle.TLabel")
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
label.pack(pady=20)

button = ttk.Button(root, text="Escuchar", style="MyStyle.TButton", command=onClick)
button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
button.pack(pady=10)

root.mainloop()