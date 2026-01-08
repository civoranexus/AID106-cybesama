from stt.stt_service import speech_to_text
from tts.tts_service import text_to_speech
from llm import generate_response

def run_voice_assistant():
    print("VoiceAid AI started")
    print("🎤 Listening...")

    text = speech_to_text(language="en")
    if not text:
        print("No speech detected")
        return

    print("You said:", text)

    response = generate_response(text)
    print("Response:", response)

    text_to_speech(response)

if __name__ == "__main__":
    run_voice_assistant()

    

