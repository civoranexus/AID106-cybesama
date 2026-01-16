# import pyttsx3

# engine = pyttsx3.init()

# def text_to_speech(text, language="en"):
#     """
#     Converts text to speech
#     """
#     engine.say(text)
#     engine.runAndWait()
#     return "AUDIO_PLAYED"

def text_to_speech(text: str) -> bytes:
    """
    Convert text response to audio bytes.
    Placeholder for TTS engine.
    """
    # TEMP: return empty bytes
    return b"VOICE_AUDIO_BYTES"
