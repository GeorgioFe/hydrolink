async function fetchSensorData() {
    try {
        const response = await fetch('/sensor-data');
        const data = await response.json();
        document.getElementById('distance').textContent = data.distance.toFixed(2);
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }
}

// Fetch sensor data every second
setInterval(fetchSensorData, 1000);
