import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join("public", "static")), name="static")

@app.get("/", response_class=HTMLResponse)
def main():
    html_file_path = os.path.join("public", "index.html")
    with open(html_file_path, 'r') as html_file:
        return html_file.read()

@app.get("/img")
def get_img():
    file_path = os.path.join("public", "static", "img.jpg")
    return FileResponse(file_path)
    
@app.get("/redirect")
def redirect_to_root():
    return RedirectResponse(url="/")