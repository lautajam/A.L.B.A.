import tkinter as tk
from tkinter import ttk

def onClick_escuchar():
    print("Escuchando")

def onClick_detener():
    print("Detenido")

#Creo la ventana y la hago no modificable en tamaño
root = tk.Tk()
root.resizable(False, False)

# Estilos
style = ttk.Style()
style.configure("MyStyle.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style.configure("MyStyleStop.TButton", font=("Arial", 14), padding=10, background="red", foreground="black")
style.configure("MyStyle.TLabel", font=("Arial", 14), padding=10, foreground="black")
root.title("A.U.R.A.")
root.geometry("800x200")

label = ttk.Label(root, text="Toca el botón para empezar la búsqueda y lectura por voz", style="MyStyle.TLabel")
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
label.pack(pady=20)

escuchar = ttk.Button(root, text="Escuchar", style="MyStyle.TButton", command=onClick_escuchar)
escuchar.pack(side=tk.LEFT, padx=(0, 50))
escuchar.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

parar = ttk.Button(root, text="Detener", style="MyStyleStop.TButton", command=onClick_detener)
parar.pack(side=tk.LEFT, padx=(50, 0))
parar.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

root.mainloop()
