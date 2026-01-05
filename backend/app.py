from stt.stt_service import speech_to_text
from nlu.nlu_service import process_text
from knowledge.knowledge_base import query_knowledge
from response.response_generator import generate_response
from tts.tts_service import text_to_speech

def handle_voice_input(audio_input, language="hi"):
    """
    Main pipeline for VoiceAid AI
    """

    # Step 1: STT
    text = speech_to_text(audio_input, language)

    # Step 2: NLU
    nlu_result = process_text(text, language)

    # Step 3: Knowledge Retrieval
    data = query_knowledge(nlu_result)

    # Step 4: Response Generation
    final_text = generate_response(data, language)

    # Step 5: TTS
    audio_output = text_to_speech(final_text, language)

    return {
        "text_response": final_text,
        "audio_response": audio_output
    }


# Temporary test
if __name__ == "__main__":
    result = handle_voice_input("आज मौसम कैसा रहेगा", "hi")
    print(result["text_response"])
