from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Scheme

app = FastAPI(title="VoiceAid AI Backend")

@app.get("/")
def root():
    return {
        "success": True,
        "message": "VoiceAid backend running",
        "source": "database"
    }
