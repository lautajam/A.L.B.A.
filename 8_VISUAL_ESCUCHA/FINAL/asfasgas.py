import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import threading

def onClick_detener():
    global detener
    detener = True

def onClick_escuchar(resultado):
    print("Escuchando")
    # Crear un objeto Recognizer
    r = sr.Recognizer()

    audio = ""

    while not detener:
        # Utilizar el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("Di algo:")
            audio = r.listen(source, timeout=500)

        # Intentar transcribir el audio
        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Transcripción:", text)
            resultado.config(text=text)  # muestra el texto escuchado en el label "resultado"
            resultado.update()  # actualiza el label para que muestre el texto inmediatamente
            if "stop" == text.lower() or "estop" == text.lower() or "es top" == text.lower():
              print("Escucha detenida")
              break
        except sr.UnknownValueError as e:
            print("No te he entendido bien!")
        except sr.RequestError as e:
            print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))

def start_listening():
    global detener
    detener = False
    # Crear un hilo para ejecutar la función onClick_escuchar
    t = threading.Thread(target=onClick_escuchar, args=(resultado,))
    t.start()

#Crea la ventana
root = tk.Tk()
root.resizable(False, False)

#Crea el componente estilos y crea los estilos
style = ttk.Style()
style.configure("MyStyle.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style.configure("MyStyleStop.TButton", font=("Arial", 14), padding=10, background="red", foreground="black")
style.configure("MyStyle.TLabel", font=("Arial", 14), padding=10, foreground="black")
root.title("A.U.R.A.")
root.geometry("800x300")

#Crea las aprtes del programa
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