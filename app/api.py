from typing import Union
import folium

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
    
def generateMap():

    m = folium.Map(location=[53.073635, 8.806422], zoom_start=15, tiles='Stamen Terrain')
    m.add_child(folium.LatLngPopup())

    m.save("templates/map.html")
    map_html = m._repr_html_()
    return {
        "map": map_html
    }

@app.get("/", response_class=HTMLResponse)
def read_root():
    return {
        "hello": "world"
    }

@app.get("/map", response_class=HTMLResponse)
async def read_item(request: Request):
    generateMap()
    return templates.TemplateResponse("index.html", {"request": request })    
