import requests
from bs4 import BeautifulSoup
import pyttsx3

# URL de la página a leer
url = "https://es.wikipedia.org/wiki/Tony_Stark_(Universo_cinematogr%C3%A1fico_de_Marvel)"

# Hacer la petición HTTP y obtener el contenido de la página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Obtener el primer párrafo del contenido principal de la página
content = soup.find("div", {"id": "mw-content-text"}).find("p")

# Obtener el texto del párrafo
text = content.get_text()

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Configurar la voz
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)  # Volumen de la voz (valor entre 0 y 1)

# Leer el texto en voz alta
engine.say(text)
engine.runAndWait()