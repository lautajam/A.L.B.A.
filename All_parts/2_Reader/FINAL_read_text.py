import pyttsx3

while 1:

    # Create an object of the pyttsx3 class.
    engine = pyttsx3.init()
    text = ""

    # Reading rate (words per minute)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1) # Voice volume (value between 0 and 1)

    print("What do you want to do?")
    selection = input(
        "Touch 1 to enter options or touch 2 to read text:")

    if selection == "1":
        words_minute = input(
            "Select the number of words per minute: ")
        # Reading rate (words per minute)
        engine.setProperty('rate', words_minute)
        volume = input("Select the volume (0 or 1): ")
        # Voice volume (value between 0 and 1)
        engine.setProperty('volume', volume)
        continue

    if selection == "2":
        while text != "#/#":
            # Get text to read aloud.
            text = input(
                "Enter the text to be read (if you want to exit type #/#): ")
            if text != "#/#":
                # Read the text aloud.
                engine.say(text)
                engine.runAndWait()
                pass
        pass