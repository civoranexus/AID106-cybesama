from fastapi import APIRouter
from voice.pipeline import run_voice_pipeline

router = APIRouter(prefix="/voice", tags=["Voice"])


@router.post("/query")
def voice_query():
    return run_voice_pipeline()


