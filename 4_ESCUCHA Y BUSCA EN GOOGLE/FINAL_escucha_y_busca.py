import webbrowser
from googlesearch import search
import speech_recognition as sr

# Crear un objeto Recognizer
r = sr.Recognizer()

while True:
    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo:")
        audio = r.listen(source, timeout=10)  # Espera 10 segundos antes de lanzar la excepción

    try:
        # Transcribir el audio en texto
        text = r.recognize_google(audio, language='es-ES')
        print("Transcripción:", text)

        # Obtener el primer resultado de la búsqueda
        escaped_text = text.replace(" ", "+")
        result = next(search(escaped_text, num_results=1))

        # Abre la página en Brave
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
        webbrowser.get('brave').open(result)
    except sr.UnknownValueError:
        print("No te he entendido bien!")
    except sr.RequestError as e:
        print("Error al conectarse con el servicio de reconocimiento de voz: {0}".format(e))
    except StopIteration:
        print("No se encontraron resultados para la búsqueda: {0}".format(text))