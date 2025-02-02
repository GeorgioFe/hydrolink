from fastapi import FastAPI, Form, Request, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import auth
import db_access as db
import main
import uvicorn
import os

app = FastAPI()

# Allow CORS for local development (adjust origins as needed for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variable to store the current interval and the WebSocket connection
current_interval = None
websocket_connection = None
latest_distance = None
calibrated_distance = None

# Mount the static files directories
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'static')), name="static")

# Route for Root.
@app.get("/", response_class=HTMLResponse)
def render_root():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'welcome.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route for About Us Page.
@app.get("/about", response_class=HTMLResponse)
def render_about():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'about.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route for Help Page.
@app.get("/help", response_class=HTMLResponse)
def render_help():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'help-support.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route for Dashboard Page.
@app.get("/dashboard", response_class=HTMLResponse)
def render_dashboard():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'dashboard.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route for Register Page.
@app.get("/register", response_class=HTMLResponse)
def render_register():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'register.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route for Login Page.
@app.get("/login", response_class=HTMLResponse)
def render_login():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'signin.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route for Sign Up Button.
@app.post("/signup", response_class=HTMLResponse)
def signup(email: str = Form(...), password: str = Form(...)):
    # Sign up user
    response = auth.user_sign_up(email, password)
    
    # HTML Content to be Returned
    content = """
    <html>
        <head>
            <script type="text/javascript">
                alert("Signup successful!");
                window.location.href = "/";
            </script>
        </head>
        <body>
        </body>
    </html>
    """
    
    return HTMLResponse(content=content, status_code=200)

# Route for Sign In Button.
@app.post("/signin", response_class=HTMLResponse)
def signin(email: str = Form(...), password: str = Form(...)):
    # Sign in user
    response = auth.user_sign_in(email, password)
    
    # HTML Content to be Returned
    content = """
    <html>
        <head>
            <script type="text/javascript">
                alert("Sign-in successful!");
                window.location.href = "/dashboard";
            </script>
        </head>
        <body>
        </body>
    </html>
    """
    
    return HTMLResponse(content=content, status_code=200)

# Route for Calculating Recommended Daily Water Intake
@app.post("/calculate_recommended_intake")
async def calculate_recommended_intake(request: Request):
    data = await request.json()
    age = int(data.get('age'))
    weight = float(data.get('weight'))
    activity = float(data.get('activity'))
    
    # Save parameters to db
    # db.set_params(age, weight, activity)
    
    # Calculate Recommended Intake
    recommended__intake = main.calculate_daily_water_intake(age, weight, activity)

    return {"intake": round(recommended__intake, 2)}

@app.post("/set_reminder")
async def set_reminder(request: Request):
    global current_interval
    body = await request.json()
    
    # Convert minutes to seconds.
    interval_str = body.get("interval")
    interval = float(interval_str)
    current_interval = interval * 60
    
    if websocket_connection:
        await websocket_connection.send_text(str(current_interval))
        
    return JSONResponse(content={"message": "Interval received", "interval": current_interval})

@app.post("/toggle_demo_mode")
async def toggle_demo_mode(request: Request):
    body = await request.json()
    demo_mode = body.get("demo_mode")
    if websocket_connection:
        message = "demo_on" if demo_mode else "demo_off"
        await websocket_connection.send_text(message)
    return JSONResponse(content={"message": f"Demo mode {'enabled' if demo_mode else 'disabled'}"})

# Route for updating the current distance from the Ultrasonic sensor.
@app.post("/distance")
async def receive_distance(request: Request):
    global latest_distance
    body = await request.json()
    distance = body.get("distance")
    latest_distance = distance
    print(f"Received distance: {latest_distance}, Calibrated distance: {calibrated_distance}")
    return JSONResponse(content={"message": "Distance received"})

# Route for calibrating the distance.
@app.post("/calibrate")
def calibrate():
    global calibrated_distance, latest_distance
    if latest_distance is not None:
        calibrated_distance = latest_distance
        print(f"Calibrated distance: {calibrated_distance}")
        return JSONResponse(content={"message": "Calibration completed", "calibrated_distance": calibrated_distance})
    else:
        return JSONResponse(content={"message": "No distance data available for calibration"}, status_code=400)

# Route to get the volume drank.
@app.get("/volume")
async def get_volume():
    latest_volume = round((latest_distance - calibrated_distance) * 1.4, 2)
    return JSONResponse(content={"latest_volume": latest_volume})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global websocket_connection
    await websocket.accept()
    websocket_connection = websocket
    try:
        while True:
            await websocket.receive_text()  # Keep the connection open
    except WebSocketDisconnect:
        websocket_connection = None

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=500)