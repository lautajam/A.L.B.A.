import speech_recognition as sr

# Create a Recognizer object
r = sr.Recognizer()

while 1:

    # Use microphone as audio source.
    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source, timeout=500) # Wait 10 seconds before throwing the exception

    # Try to transcribe the audio
    try:
        text = r.recognize_google(audio, language='en-ES')
        print("Transcription:", text)
    except sr.UnknownValueError as e:
        print("I didn't understand you correctly!")
    except sr.RequestError as e:
        print("Error connecting to speech recognition service; {0}".format(e))
