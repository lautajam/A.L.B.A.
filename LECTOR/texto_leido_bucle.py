import pyttsx3

while 1:

    # Crear un objeto de la clase pyttsx3
    engine = pyttsx3.init()
    texto = ""

    # Velocidad de lectura (palabras por minuto)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)  # Volumen de la voz (valor entre 0 y 1)

    print("¿Qué quiere hacer?")
    seleccion = input(
        "Toque 1 para entrar en opciones o toque 2 para leer texto: ")

    if seleccion == "1":
        palabras_minuto = input(
            "Seleccione la cantidad de palabras por minuto: ")
        # Velocidad de lectura (palabras por minuto)
        engine.setProperty('rate', palabras_minuto)
        volumen = input("Seleccione el volumen (0 o 1): ")
        # Volumen de la voz (valor entre 0 y 1)
        engine.setProperty('volume', volumen)
        continue

    elif seleccion == "2":
        while texto != "#/#":
            # Obtener el texto a leer en voz alta
            texto = input(
                "Introduce el texto a leer (si quieres salir escribe #/#): ")
            if texto != "#/#":
                # Leer el texto en voz alta
                engine.say(texto)
                engine.runAndWait()
                pass
        pass