from fastapi import APIRouter, HTTPException, Query
from typing import List
from ..models.flight import FlightResponse
from ..services import flight_service

router = APIRouter()

@router.get("/flights/search", response_model=List[FlightResponse])
def search_flights(
    origin: str = Query(..., min_length=3, max_length=3),
    destination: str = Query(..., min_length=3, max_length=3),
):
    try:
        flights = flight_service.find_flights_from_api(origin, destination)
        return flights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))