import webbrowser
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import pyttsx3

query = input("¿Que quiere buscar en google? ")  # define la consulta de búsqueda

# Obtén el primer resultado de la búsqueda
result = next(search(query, num_results=1))

# Hacer la petición HTTP y obtener el contenido de la página
response = requests.get(result)
soup = BeautifulSoup(response.content, 'html.parser')

# Obtener los párrafos de la página
paragraphs = soup.find_all('p')

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Configurar la voz
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)  # Volumen de la voz (valor entre 0 y 1)

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