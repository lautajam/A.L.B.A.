import tkinter as tk
from tkinter import ttk
from funciones import onClick_detener, onClick_escuchar, start_listening

# Crea la ventana
root = tk.Tk()
root.resizable(False, False)

# Crea el componente estilos y crea los estilos
style = ttk.Style()
style.configure("MyStyle.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style.configure("MyStyleStop.TButton", font=("Arial", 14), padding=10, background="red", foreground="black")
style.configure("MyStyle.TLabel", font=("Arial", 14), padding=10, foreground="black")
root.title("A.L.B.A.")
root.geometry("800x350")

# Crea las aprtes del programa
label = ttk.Label(root, text="Toca el botón para empezar la búsqueda y lectura por voz", style="MyStyle.TLabel")
label.pack(pady=(10,0))

label2 = ttk.Label(root, text="(Si quiere detener la escucha solo diga 'Stop')", style="MyStyle.TLabel")
label2.pack(pady=(0,20))

frame = ttk.Frame(root)
frame.pack()

resultado = ttk.Label(root, text="--- ", style="MyStyle.TLabel")
resultado.pack(pady=(10, 0))

escuchando = ttk.Label(root, text="Sin escuchar", style="MyStyle.TLabel")
escuchando.pack(pady=(5, 0))

donde_busca = ttk.Label(root, text="aaaaaaaaaaaaa", style="MyStyle.TLabel")
donde_busca.pack(pady=(5, 0))

escuchar = ttk.Button(frame, text="Escuchar", style="MyStyle.TButton", command=lambda:start_listening(resultado, escuchando))
escuchar.pack(side=tk.LEFT, padx=(0, 30))

parar = ttk.Button(frame, text="Detener lectura", style="MyStyleStop.TButton", command=onClick_detener)
parar.pack(side=tk.LEFT, padx=(30, 0))

root.mainloop()