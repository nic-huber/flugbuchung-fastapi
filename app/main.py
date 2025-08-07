from fastapi import FastAPI
from .routers import flights

app = FastAPI(
    title="Flugbuchungs-API",
    description="Eine API zur Suche nach Flugdaten.",
    version="1.0.0",
)

app.include_router(flights.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Willkommen zur Flugbuchungs-API!"}