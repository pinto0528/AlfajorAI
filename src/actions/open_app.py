import os
from assistant.tts import speak

def open_application(command):
    if "chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    # Añade más aplicaciones según sea necesario
