import webbrowser
from googlesearch import search

query = input("¿Que quiere buscar en google? ")  # define la consulta de búsqueda

# Obtén el primer resultado de la búsqueda
result = next(search(query, num_results=1))

# Abre la página en Brave
webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
webbrowser.get('brave').open(result)