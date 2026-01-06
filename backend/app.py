from stt.stt_service import speech_to_text
from nlu.nlu_service import process_text
from knowledge.knowledge_base import query_knowledge
from response.response_generator import generate_response
from tts.tts_service import text_to_speech

def run_voice_assistant():
    print("VoiceAid AI started")

    text = speech_to_text(language="hi")
    print("You said:", text)

    nlu_result = process_text(text)
    print("Intent:", nlu_result["intent"])

    data = query_knowledge(nlu_result)
    response_text = generate_response(data, nlu_result["language"])

    print("Response:", response_text)
    text_to_speech(response_text)

if __name__ == "__main__":
    run_voice_assistant()
