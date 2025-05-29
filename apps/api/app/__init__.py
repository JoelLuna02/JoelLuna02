"""Archivo principal de la aplicación FastAPI."""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from database.config import engine
import database.models as model

app = FastAPI()
templates = Jinja2Templates(directory="html")
app.mount("/static", StaticFiles(directory="public"), name="static")
model.Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    """Renderiza la página principal."""
    return templates.TemplateResponse("main_page.html", {"request": request})
