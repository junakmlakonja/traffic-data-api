from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import models
from .database import SessionLocal, engine

# Kreiranje tabela u bazi (ako već nisu kreirane)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Traffic Data API")

# --- SCHEMA (Pydantic model za proveru podataka) ---
class TrafficCreate(BaseModel):
    segment_id: str
    speed: float
    travel_time: int

# --- DATABASE DEPENDENCY (Otvara vezu sa bazom za svaki poziv) ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTS ---

@app.get("/", tags=["Health"])
def root():
    return {"message": "API radi!"}

@app.post("/traffic", tags=["Data"])
def create_traffic_record(data: TrafficCreate, db: Session = Depends(get_db)):
    # 1. Pravimo objekat za bazu
    new_record = models.TrafficRecord(
        segment_id=data.segment_id,
        speed=data.speed,
        travel_time=data.travel_time
    )
    # 2. Snimamo u bazu
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"status": "success", "data": new_record}

from sqlalchemy import func

@app.get("/traffic/analytics/average-speed", tags=["Analytics"])
def get_average_speed(db: Session = Depends(get_db)):
    # SQL query: SELECT AVG(speed) FROM traffic_records
    avg_speed = db.query(func.avg(models.TrafficRecord.speed)).scalar()
    
    if avg_speed is None:
        return {"message": "Nema podataka u bazi još uvek."}
        
    return {
        "average_speed": round(avg_speed, 2),
        "unit": "km/h",
        "status": "calculated_from_live_data"
    }

@app.get("/traffic/analytics/congestion", tags=["Analytics"])
def get_congestion_report(db: Session = Depends(get_db)):
    # Uzimamo sve zapise gde je brzina manja od 20 km/h
    congested_segments = db.query(models.TrafficRecord).filter(models.TrafficRecord.speed < 20).all()
    
    return {
        "congestion_level": "High" if len(congested_segments) > 0 else "Low",
        "congested_segments_count": len(congested_segments),
        "details": congested_segments
    }

@app.get("/health")
def health():
    return {"status": "ok"}