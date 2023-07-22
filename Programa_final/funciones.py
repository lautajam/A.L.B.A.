import threading
import webbrowser
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

def onClick_detener(resultado, escuchando, donde_busca):
    print("Lectura detenida")
    escuchando.config(text="Escuchando | Lectura detenida")
    escuchando.update()

    donde_busca.config(text="Busquda en: ---")
    donde_busca.update()

    resultado.config(text="Transcripción: ---")
    resultado.update()

def busquedaLectura(text, donde_busca, escuchando):

    # Llamar globables
    # Crear un objeto Recognize
    r = sr.Recognizer()

    r.pause_threshold = 5
    global engine

    # Configurar la voz
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)  # Volumen de la voz (valor entre 0 y 1)
    
    # Obtén el primer resultado de la búsqueda
    result = next(search(text, num_results=1))

    print(result)

    donde_busca.config(text="Busqueda en: " + result)
    donde_busca.update()

    # Hacer la petición HTTP y obtener el contenido de la página
    response = requests.get(result)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Obtener los párrafos de la página
    paragraphs = soup.find_all('p')

    # Abre la página en Brave
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
    webbrowser.get('brave').open(result)

    # Leer los párrafos en voz alta hasta que aparezca otra etiqueta
    for paragraph in paragraphs:
        text = paragraph.get_text()
        engine.say(text)
        
        # Verificar si hay otra etiqueta después del párrafo actual
        next_sibling = paragraph.find_next_sibling()
        if next_sibling is not None and next_sibling.name != 'p':
            break

    # Ejecutar la lectura
    engine.runAndWait()

def onClick_escuchar(resultado, escuchando, donde_busca):

    print("Escuchando")
    escuchando.config(text="Escuchando")
    escuchando.update()

    print("Busqueda en: ---")
    donde_busca.config(text="Busquda en: ---")
    donde_busca.update()

    # Crear un objeto Recognizer
    r = sr.Recognizer()
    audio = ""

    while 1:
        # Utilizar el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("¿Qué quieres que busque? ")
            audio = r.listen(source, timeout=500)

        # Intentar transcribir el audio
        try:
            text = r.recognize_google(audio, language='es-ES')
            print("Transcripción: ", text)
            print("Escuchando")
            resultado.config(text="Transcripción: " + text)  # muestra el texto escuchado en el label "resultado"
            resultado.update()  # actualiza el label para que muestre el texto inmediatamente
            busquedaLectura(text, donde_busca, escuchando)
            if "stop" == text.lower() or "estop" == text.lower() or "es top" == text.lower():
                print("Escucha detenida")
                resultado.config(text="Transcripción: " + text)  # muestra el texto escuchado en el label "resultado"
                escuchando.config(text="Escucha detenida")
                donde_busca.config(text="Busquda en: ---")
                resultado.update()  # actualiza el label para que muestre el texto inmediatamente
                escuchando.update()
                donde_busca.update()
                break
        except sr.UnknownValueError as e:
            print("No te he entendido bien!")
            resultado.config(text="No te he entendido bien!")
            resultado.update()
        except sr.RequestError as e:
            print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))

def start_listening(resultado, escuchando, donde_busca):
    # Crear un hilo para ejecutar la función onClick_escuchar
    t = threading.Thread(target=onClick_escuchar, args=(resultado,escuchando,donde_busca,))
    t.start()

def stop_reading(resultado, escuchando, donde_busca):
    # Crear un hilo para ejecutar la función onClick_escuchar
    t = threading.Thread(target=onClick_detener, args=(resultado, escuchando, donde_busca,))
    t.start()