
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Peninah. This is the Actuator Project"}

@app.get("/sum")
async def sum():
    return {"message": "Hello Peninah. This is the sum"}


from fastapi import FastAPI
from uvicorn import Server

from uvicorn.config import Config
from pyctuator.pyctuator import Pyctuator


app_name = "FastAPI App with Pyctuator"
app = FastAPI(title=app_name)


@app.get("/")
def hello():
    return "Hello World!"


Pyctuator(
    app,
    "FastAPI Pyctuator",
    app_url="http://localhost:8000",
    pyctuator_endpoint_url="http://host.docker.internal:8000/pyctuator",
    registration_url="http://localhost:8080/instances"
)

Server(config=(Config(app=app, loop="asyncio"))).run()