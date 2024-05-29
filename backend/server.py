from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

# Mount the static files directories
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), '..', 'frontend', 'static')), name="static")

# Route to Root
@app.get("/", response_class=HTMLResponse)
def render_root():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'welcome.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route to About Us
@app.get("/about", response_class=HTMLResponse)
def render_about():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'about.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route to Help
@app.get("/help", response_class=HTMLResponse)
def render_help():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'help-support.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Route to Help
@app.get("/register", response_class=HTMLResponse)
def render_help():
    # Using a relative path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'pages', 'register.html')
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=500)