from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app.mount("/static", StaticFiles(directory="."), name="static")  # serve files from root

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html") as f:
        return HTMLResponse(content=f.read())
