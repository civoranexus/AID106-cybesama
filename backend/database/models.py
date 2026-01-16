from sqlalchemy import Column, Integer, String, Text, Date, Numeric, TIMESTAMP
from sqlalchemy.sql import func
from .db import Base

# -------------------------------
# Government Schemes
# -------------------------------
class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(Text)
    eligibility = Column(Text)
    benefits = Column(Text)
    source_url = Column(String)
    last_updated = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

# -------------------------------
# Crop Prices
# -------------------------------
class CropPrice(Base):
    __tablename__ = "crop_prices"

    id = Column(Integer, primary_key=True, index=True)
    crop_name = Column(String, nullable=False, index=True)
    mandi = Column(String)
    price_per_quintal = Column(Numeric)
    date = Column(Date)

# -------------------------------
# Weather Data (cached API)
# -------------------------------
class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    temperature = Column(Numeric)
    rainfall = Column(Numeric)
    recorded_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
