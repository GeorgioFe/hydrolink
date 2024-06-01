from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import auth
import uvicorn
import os

app = FastAPI()

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

# Route for Sign In Page.
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

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=500)