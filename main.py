from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from engine import Engine

app = FastAPI()
engine = Engine()

# WordPress izin versin diye (çok önemli)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
def analyze(data: dict):
    return engine.evaluate(data)