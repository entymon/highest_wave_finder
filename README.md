## Working locally on the app

1. Create local virtual env
`python -m venv venv`

2. Link to that environment
`source ./venv/bin/activate`

3. then run command
`uvicorn app.api:app` - run an app http://127.0.0.1:8000

## Working with Docker

1. Build image
`docker buildx build -t high-wave:1 .`

2. Run container
- `docker run -p 8080:8080 high-wave:1` OR
- `docker run -d --name high-wave-container -p 8080:8080 high-wave:1` // run in background

3. The environment should be available under URL: `http://0.0.0.0:8080`

## Useful links
- [Folium](https://python-visualization.github.io/folium/)
- [xArray](https://docs.xarray.dev/en/stable/index.html)
- [FastAPI](https://fastapi.tiangolo.com/lo/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/#template-inheritance)

## Useful command

Dump libs - run on virtual environment
- `pip freeze > requirements.txt`



