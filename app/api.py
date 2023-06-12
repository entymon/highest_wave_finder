from typing import Union
import folium
import xarray as xr
import numpy as np

from jinja2 import Template
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from folium.features import LatLngPopup

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Redirect(LatLngPopup):
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    window.location="/?lat=" + e.latlng.lat.toFixed(7) + "&lng=" + e.latlng.lng.toFixed(7);
                }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)

    def __init__(self):
        super(Redirect, self).__init__()
        self._name = 'Redirect'
    
def generate_map(lat: float = 53.073635, lng: float = 8.806422):

    m = folium.Map(location=[lat, lng], zoom_start=5, tiles='Stamen Terrain')

    Redirect().add_to(m)

    folium.Marker(
        location=[lat, lng],
        popup="Latitude: " + str(lat) + "; Longitude: " + str(lng) + "",
    ).add_to(m)

    m.save("templates/map.html")
    map_html = m._repr_html_()
    return {
        "map": map_html
    }

def get_highest_wave(lat: float = 53.073635, lng: float = 8.80): 

    ds = xr.open_dataset("waves_data/waves_2019-01-01.nc")
    wave_spot = ds.sel(latitude=lat, longitude=lng, method="nearest")
    max_waves_data = np.array(wave_spot.hmax.data)

    height_max = round(max_waves_data.max(), 2)

    if height_max:
        return height_max
    else:
        return 0

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, lat: str = '0', lng: str = '0'):

    h_max = "0"
    if lat != '0':
        h_max = str(get_highest_wave(lat, lng))

    template_data = { 
        "request": request,
        "latitude": lat,
        "longitude": lng,
        "h_max": h_max
    }

    generate_map(float(lat), float(lng))
    return templates.TemplateResponse("index.html", template_data)    


