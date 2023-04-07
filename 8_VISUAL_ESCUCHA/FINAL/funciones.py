import threading
import speech_recognition as sr

def onClick_detener():
    print("Lectura detenida")

def onClick_escuchar(resultado, escuchando):
    print("Escuchando")
    escuchando.config(text="Escuchando")  # muestra el texto escuchado en el label "resultado"
    escuchando.update()
    resultado.config(text="Transcripción:: ")
    resultado.update()
    # Crear un objeto Recognizer
    r = sr.Recognizer()

    audio = ""

    while 1:
        # Utilizar el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("Di algo:")
            audio = r.listen(source, timeout=500)

        # Intentar transcribir el audio
        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Transcripción: ", text)
            resultado.config(text="Transcripción: " + text)  # muestra el texto escuchado en el label "resultado"
            resultado.update()  # actualiza el label para que muestre el texto inmediatamente
            if "stop" == text.lower() or "estop" == text.lower() or "es top" == text.lower():
                print("Escucha detenida")
                resultado.config(text="Transcripción: " + text)  # muestra el texto escuchado en el label "resultado"
                resultado.update()  # actualiza el label para que muestre el texto inmediatamente
                escuchando.config(text="Escucha detenida")
                escuchando.update()
                break
        except sr.UnknownValueError as e:
            print("No te he entendido bien!")
            resultado.config(text="No te he entendido bien!")
            resultado.update()
        except sr.RequestError as e:
            print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))

def start_listening(resultado, escuchando):
    # Crear un hilo para ejecutar la función onClick_escuchar
    t = threading.Thread(target=onClick_escuchar, args=(resultado,escuchando,))
    t.start()