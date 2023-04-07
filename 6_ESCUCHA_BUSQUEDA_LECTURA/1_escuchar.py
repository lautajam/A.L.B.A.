import speech_recognition as sr

# Crear un objeto Recognizer
r = sr.Recognizer()

while 1:

    # Utilizar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo:")
        audio = r.listen(source, timeout=500)  # Espera 10 segundos antes de lanzar la excepción

    # Intentar transcribir el audio
    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Transcripción:", text)
    except sr.UnknownValueError as e:
        print("No te he entendido bien!")
    except sr.RequestError as e:
        print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))
