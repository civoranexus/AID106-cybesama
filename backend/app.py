from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from voice.voice import router as voice_router

app = FastAPI(title="VoiceAid AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router)


@app.get("/")
def health():
    return {"status": "VoiceAid backend running"}


    

