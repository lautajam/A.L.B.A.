import pyttsx3

# Create an object of the pyttsx3 class
engine = pyttsx3.init()

# Get the text to read aloud
text = input("Enter the text to read: ")

# Configure the speed and volume of the voice
engine.setProperty('rate', 150) # Reading rate (words per minute)
engine.setProperty('volume', 1) # Voice volume (value between 0 and 1)

# Read text aloud
engine.say(text)
engine.runAndWait()