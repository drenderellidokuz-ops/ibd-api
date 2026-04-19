from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Patient(BaseModel):
    crp: float
    calprotectin: float
    blood_in_stool: bool

@app.post("/analyze")
def analyze(p: Patient):
    risk = "low"

    if p.crp > 50 or p.calprotectin > 300:
        risk = "high"

    if p.blood_in_stool:
        risk = "high"

    return {"risk": risk}