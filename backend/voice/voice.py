from fastapi import APIRouter
from pydantic import BaseModel
from voice.pipeline import handle_voice_request

router = APIRouter(prefix="/voice", tags=["voice"])


class VoiceQueryRequest(BaseModel):
    text: str
    user_context: dict = {}


@router.post("/query")
def voice_query(payload: VoiceQueryRequest):
    return handle_voice_request(
        text=payload.text,
        user_context=payload.user_context
    )
