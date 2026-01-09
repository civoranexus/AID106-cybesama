from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Scheme

def seed_schemes(db: Session):
    schemes = [
        Scheme(
            name="PM-KISAN",
            description="Pradhan Mantri Kisan Samman Nidhi is a central sector scheme to provide income support to farmers.",
            eligibility="Small and marginal farmers owning cultivable land.",
            benefits="₹6000 per year in three equal installments.",
            source_url="https://pmkisan.gov.in/"
        ),
        Scheme(
            name="PMFBY",
            description="Pradhan Mantri Fasal Bima Yojana provides crop insurance against natural calamities.",
            eligibility="All farmers growing notified crops in notified areas.",
            benefits="Insurance coverage with low premium rates.",
            source_url="https://pmfby.gov.in/"
        )
    ]

    for scheme in schemes:
        exists = db.query(Scheme).filter(Scheme.name == scheme.name).first()
        if not exists:
            db.add(scheme)

    db.commit()

def run():
    db = SessionLocal()
    try:
        seed_schemes(db)
        print("✅ Scheme seed data inserted successfully")
    finally:
        db.close()

if __name__ == "__main__":
    run()
