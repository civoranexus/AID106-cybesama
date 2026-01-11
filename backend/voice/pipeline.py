from voice.stt_service import speech_to_text
from voice.tts_service import text_to_speech
from routing.router import route_query


from typing import Optional


def handle_voice_request(
    *,
    text: Optional[str] = None,
    audio_bytes: Optional[bytes] = None,
    user_context: Optional[dict] = None
):
    """
    Voice pipeline (LLM-free)

    Accepts:
    - text (preferred for Step 7 frontend)
    - audio_bytes (future backend STT)

    Returns:
    - structured text response
    - audio output (base64 / bytes)
    """

    user_context = user_context or {}

    # 1. Get text
    if text:
        query_text = text
    elif audio_bytes:
        query_text = speech_to_text(audio_bytes)
    else:
        return {"error": "No input provided"}

    # 2. Route query (deterministic logic)
    response = route_query(query_text, user_context)

    # 3. Prepare spoken output
    spoken_text = response.message

    if hasattr(response, "summary") and response.summary:
        spoken_text += " " + response.summary

    # 4. TTS
    audio_output = text_to_speech(spoken_text)

    # 5. Return JSON-safe structure
    return {
        "query": query_text,
        "text_response": {
            "message": response.message,
            "summary": getattr(response, "summary", None),
            "data": getattr(response, "data", None),
        },
        "audio_response": audio_output,
    }


