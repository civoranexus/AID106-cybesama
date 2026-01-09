from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

print("🚀 main.py loaded")

from database.db import get_db
from database.models import Scheme

app = FastAPI()

@app.get("/")
def root():
    return {"status": "VoiceAid backend running"}

@app.get("/schemes/{scheme_name}")
def get_scheme(scheme_name: str, db: Session = Depends(get_db)):
    scheme = (
        db.query(Scheme)
        .filter(Scheme.name.ilike(f"%{scheme_name}%"))
        .first()
    )

    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")

    return {
        "name": scheme.name,
        "eligibility": scheme.eligibility,
        "benefits": scheme.benefits,
        "source_url": scheme.source_url
    }
