from typing import Union
import folium
from folium.features import LatLngPopup

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Template

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class GetLatLngPopup(LatLngPopup):
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent("Latitude: " + e.latlng.lat.toFixed(7) +
                                    "<br>Longitude: " + e.latlng.lng.toFixed(7) +
                                    "<br><a href='/?lat=" + e.latlng.lat.toFixed(7) + "&lng=" + e.latlng.lng.toFixed(7) + "'>get wave</a>")
                        .openOn({{this._parent.get_name()}});
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)

    def __init__(self):
        super(GetLatLngPopup, self).__init__()
        self._name = 'GetLatLngPopup'
    
def generate_map():

    m = folium.Map(location=[53.073635, 8.806422], zoom_start=15, tiles='Stamen Terrain')
    # m.add_child(folium.LatLngPopup())

    GetLatLngPopup().add_to(m)

    m.save("templates/map.html")
    map_html = m._repr_html_()
    return {
        "map": map_html
    }

@app.get("/hello", response_class=HTMLResponse)
def read_root():
    return {
        "hello": "world"
    }

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    generate_map()
    return templates.TemplateResponse("index.html", {"request": request })    
