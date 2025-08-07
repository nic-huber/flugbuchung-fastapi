import requests
from typing import List
from ..models.flight import FlightResponse
import os

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
API_URL = "http://api.aviationstack.com/v1/flights"

def find_flights_from_api(origin: str, destination: str) -> List[FlightResponse]:
    params = {
        "access_key": API_KEY,
        "dep_iata": origin,
        "arr_iata": destination,
        "flight_status": "scheduled"
    }

    print(f"Abfrage der Aviationstack API mit Parametern: {params}")

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        
        flights_data = response.json().get("data", [])
        
        parsed_flights = []
        for flight in flights_data:
            parsed_flights.append(
                FlightResponse(
                    flight_number=flight.get("flight", {}).get("iata"),
                    airline=flight.get("airline", {}).get("name"),
                    origin=flight.get("departure", {}).get("iata"),
                    destination=flight.get("arrival", {}).get("iata"),
                    departure_time=flight.get("departure", {}).get("scheduled"),
                    arrival_time=flight.get("arrival", {}).get("scheduled"),
                    price=400.00
                )
            )
        return parsed_flights

    except requests.exceptions.RequestException as e:
        print(f"Fehler bei der API-Anfrage: {e}")
        return []
    except Exception as e:
        print(f"Fehler beim Parsen der Daten: {e}")
        return []