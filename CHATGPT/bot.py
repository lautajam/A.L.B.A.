from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re

# Seteamos la consulta que deseamos realizar
query = "como se llama la abuela en esperando"

# Ejecutamos la búsqueda
results = search(query, num_results=1)

# Obtenemos la URL del primer resultado
url = next(iter(results), '')

# Descargamos el contenido de la página
response = requests.get(url)

# Extraemos el texto de la página
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

# Limpiamos el texto de caracteres especiales
text = re.sub(r'\s+', ' ', text)

# Imprimimos el texto
print(text)