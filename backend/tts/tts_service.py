import pyttsx3

engine = pyttsx3.init()

def text_to_speech(text, language="en"):
    """
    Converts text to speech
    """
    engine.say(text)
    engine.runAndWait()
    return "AUDIO_PLAYED"
