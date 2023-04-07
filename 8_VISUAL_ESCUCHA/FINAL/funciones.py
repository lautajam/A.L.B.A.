import speech_recognition as sr
import threading

def onClick_escuchar():
    print("Escuchando")
    # Crear un objeto Recognizer
    r = sr.Recognizer()

    audio = ""

    while audio != "Detener escucha":
        # Utilizar el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("Di algo:")
            audio = r.listen(source, timeout=500)

        # Intentar transcribir el audio
        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Transcripción:", text)
            if "stop" == text.lower() or "estop" == text.lower() or "es top" == text.lower():
              print("Escucha detenida")
              break
        except sr.UnknownValueError as e:
            print("No te he entendido bien!")
        except sr.RequestError as e:
            print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))

def start_listening():
    # Crear un hilo para ejecutar la función onClick_escuchar
    t = threading.Thread(target=onClick_escuchar)
    t.start()

def onClick_detener():
    print("Lectura detenida")