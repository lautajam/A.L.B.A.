import pyttsx3
engine = pyttsx3.init()
# Crear un objeto de la clase pyttsx3

# Obtener el texto a leer en voz alta
texto = input("Introduce el texto a leer: ")

# Configurar la velocidad y el volumen de la voz
engine.setProperty('rate', 150)  # Velocidad de lectura (palabras por minuto)
engine.setProperty('volume', 1)  # Volumen de la voz (valor entre 0 y 1)

# Leer el texto en voz alta
engine.say(texto)
engine.runAndWait()