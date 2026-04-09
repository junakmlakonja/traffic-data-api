from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class TrafficRecord(Base):
    __tablename__ = "traffic_records"

    id = Column(Integer, primary_key=True, index=True)
    segment_id = Column(String, index=True)  # ID deonice puta
    speed = Column(Float)                     # Trenutna brzina
    travel_time = Column(Integer)             # Vreme putovanja u sekundama
    timestamp = Column(DateTime(timezone=True), server_default=func.now()) # Kada je podatak stigao
