Run docker build:
`docker buildx build -t high-wave:1 . `

Run docker
`docker run -d --name high-wave-container  -p 8080:8080 high-wave:1`

## Working locally on the app

1. Create local virtual env
`python -m venv venv`

2. Link to that environment
`source ./venv/bin/activate`

3. then run command
`uvicorn app.api:app` - run an app http://127.0.0.1:8000

## Dump libs
`pip freeze > requirements.txt`

## Working with Docker

1. Build image
`docker buildx build -t high-wave:1 .`

2. Run container
`docker run -p 8080:8080 high-wave:1`

OR

`docker run -d --name high-wave-container -p 8080:8080 high-wave:1` // run in background

3. The environment should be available under URL: `http://0.0.0.0:8080`