import tkinter as tk
from tkinter import ttk
from funciones import onClick_detener, onClick_escuchar, start_listening

root = tk.Tk()
root.resizable(False, False)

style = ttk.Style()
style.configure("MyStyle.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style.configure("MyStyleStop.TButton", font=("Arial", 14), padding=10, background="red", foreground="black")
style.configure("MyStyle.TLabel", font=("Arial", 14), padding=10, foreground="black")
root.title("A.U.R.A.")
root.geometry("800x200")

label = ttk.Label(root, text="Toca el botón para empezar la búsqueda y lectura por voz", style="MyStyle.TLabel")
label.pack(pady=(10,0))

label2 = ttk.Label(root, text="(Si quiere detener la escucha solo diga 'Stop')", style="MyStyle.TLabel")
label2.pack(pady=(0,20))

frame = ttk.Frame(root)
frame.pack()

escuchar = ttk.Button(frame, text="Escuchar", style="MyStyle.TButton", command=start_listening)
escuchar.pack(side=tk.LEFT, padx=(0, 30))

parar = ttk.Button(frame, text="Detener lectura", style="MyStyleStop.TButton", command=onClick_detener)
parar.pack(side=tk.LEFT, padx=(30, 0))

resultado = ttk.Label(root, text="", style="MyStyle.TLabel")
resultado.pack(pady=(10, 0))

root.mainloop()