from dotenv import load_dotenv # 1. Importiere die Funktion zum Laden der .env-Datei
load_dotenv()                 # 2. Lade die Umgebungsvariablen

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.flights import router

app = FastAPI(
    title="Flugbuchungs-API",
    description="Eine API zur Suche nach Flugdaten.",
    version="1.0.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Willkommen zur Flugbuchungs-API!"}