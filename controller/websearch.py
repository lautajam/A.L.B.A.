import webbrowser
from googlesearch import search


def web_search():
    """
    This function searches for the input query in google and opens the first result in Brave
    
    Parameters:
        None

    Returns:
        Open the first result of the search in Brave browser
    """
    query = input("What do you want to search in google? ")

    # get the first result of the search
    result = next(search(query, num_results=1))

    # Open the page in Brave
    webbrowser.register('brave', 
                        None, 
                        webbrowser.BackgroundBrowser("C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"))

    webbrowser.get('brave').open(result)