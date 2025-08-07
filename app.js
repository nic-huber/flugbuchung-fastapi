document.getElementById('search-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const origin = document.getElementById('origin').value;
    const destination = document.getElementById('destination').value;

    const url = `http://127.0.0.1:8000/api/v1/flights/search?origin=${origin}&destination=${destination}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Netzwerk-Antwort war nicht ok. Status: ${response.status}`);
        }
        const flights = await response.json();
        
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        if (flights.length === 0) {
            resultsDiv.innerHTML = '<p>Keine Flüge gefunden.</p>';
        } else {
            flights.forEach(flight => {
                const flightItem = document.createElement('div');
                flightItem.className = 'flight-item';
                flightItem.innerHTML = `
                    <strong>${flight.airline} ${flight.flight_number}</strong><br>
                    Flug von ${flight.origin} nach ${flight.destination}<br>
                    Abflug: ${new Date(flight.departure_time).toLocaleString()}<br>
                    Ankunft: ${new Date(flight.arrival_time).toLocaleString()}<br>
                    Preis: ${flight.price.toFixed(2)} €
                `;
                resultsDiv.appendChild(flightItem);
            });
        }
    } catch (error) {
        console.error('Fehler beim Abrufen der Flugdaten:', error);
        document.getElementById('results').innerHTML = `<p>Ein Fehler ist aufgetreten: ${error.message}</p>`;
    }
});