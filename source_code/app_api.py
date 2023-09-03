
#from fastapi import FastAPI
#app = FastAPI()


#@app.get("/")
#async def root():
   # return {"message": "Hello Peninah. This is the Actuator Project"}

#@app.get("/sum")
#async def sum():
   # return {"message": "Hello Peninah. This is the sum"}


from fastapi import FastAPI
from uvicorn import Server
from uvicorn import run
from uvicorn.config import Config
from pyctuator.pyctuator import Pyctuator
import requests  # Import requests library for HTTP requests


app_name = "FastAPI App with Pyctuator"
app = FastAPI(title=app_name)


@app.get("/")
def hello():
    return "Hello World!"


try:
    # Attempt to register with the "boot-admin" server
    registration_response = requests.post("http://localhost:8080/instances")
    registration_response.raise_for_status()  # Raise an exception if the registration fails
    print("Registered with boot-admin successfully")
except requests.exceptions.RequestException as e:
    print(f"Failed to register with boot-admin: {e}")

Pyctuator(
    app,
    "FastAPI Pyctuator",
    app_url="http://localhost:8000",
    pyctuator_endpoint_url="http://host.docker.internal:8000/pyctuator",
    registration_url="http://localhost:8080/instances"
)
#Server(config=(Config(app=app, loop="asyncio"))).run()

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)


