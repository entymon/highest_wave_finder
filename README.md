Setup environment:

1. Install `pipenv` python package manager: `sudo -H pip install -U pipenv`

Setup project:
- `pipenv install` to install all the required packages for the project
- `pipenv run python hello.py`

Run docker build:
`docker buildx build -t high-wave:1 . `

Run docker
`docker run -d --name high-wave-container  -p 8080:8080 high-wave:1`


`pip freeze > requirements.txt`

## Working locally on the app

1. Create local virtual env
`python -m venv venv`

2. Link to that environment
`source ./venv/bin/activate`

3. then run command

`uvicorn app.main:app` - run an app http://127.0.0.1:8000



## Wtih pipenv
1. `pipenv shell`
