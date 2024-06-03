from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import threading
import serial

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

class SensorData(BaseModel):
    distance: float

sensor_data = SensorData(distance=0.0)

bt_port = 'COM12'  # Update this to your port
baud_rate = 115200
ser = serial.Serial(bt_port, baud_rate, timeout=1)

def read_from_bluetooth():
    global sensor_data
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            try:
                distance = float(data)
                sensor_data.distance = distance
            except ValueError:
                continue

threading.Thread(target=read_from_bluetooth, daemon=True).start()

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html", "r") as file:
        return HTMLResponse(content=file.read())

@app.get("/sensor-data")
def get_sensor_data():
    return sensor_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
