import webbrowser
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
 
# Crear un objeto Recognizer
r = sr.Recognizer()

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Configurar la voz
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)  # Volumen de la voz (valor entre 0 y 1)

while True:

    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("¿Que quiere buscar en google? ")
        query = r.listen(source, timeout=10)  # Espera 10 segundos antes de lanzar la excepción

    # Intentar transcribir el audio
    try:
        text = r.recognize_google(query, language='es-ES')
        print("Transcripción:", text)
    except sr.UnknownValueError as e:
        print("No te he entendido bien!")
        continue
    except sr.RequestError as e:
        print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))
        continue

    # Obtén el primer resultado de la búsqueda
    result = next(search(text, num_results=1))

    print(result)

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