from pydantic import BaseModel
from datetime import datetime

class FlightResponse(BaseModel):
    flight_number: str | None
    airline: str | None
    origin: str | None
    destination: str | None
    departure_time: datetime | None
    arrival_time: datetime | None
    price: float | None