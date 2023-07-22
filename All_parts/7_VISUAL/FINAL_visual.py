import tkinter as tk
from tkinter import ttk

def onClick_listen():
    print("Escuchando")

def onClick_stop():
    print("Detenido")

#I create the window and make it non-modifiable in size
root = tk.Tk()
root.resizable(False, False)

# Styles
style = ttk.Style()
style.configure("MyStyle.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style.configure("MyStyleStop.TButton", font=("Arial", 14), padding=10, background="red", foreground="black")
style.configure("MyStyle.TLabel", font=("Arial", 14), padding=10, foreground="black")
root.title("A.U.R.A.")
root.geometry("800x200")

label = ttk.Label(root, text="Toca el botón para empezar la búsqueda y lectura por voz", style="MyStyle.TLabel")
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
label.pack(pady=20)

escuchar = ttk.Button(root, text="Escuchar", style="MyStyle.TButton", command=onClick_listen)
escuchar.pack(side=tk.LEFT, padx=(0, 50))
escuchar.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

parar = ttk.Button(root, text="Detener", style="MyStyleStop.TButton", command=onClick_stop)
parar.pack(side=tk.LEFT, padx=(50, 0))
parar.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

root.mainloop()
