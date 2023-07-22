import webbrowser
from googlesearch import search

query = input("What do you want to search in google? ") # define search query

# get the first result of the search
result = next(search(query, num_results=1))

# Open the page in Brave
webbrowser.register('brave', None, webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))
webbrowser.get('brave').open(result)