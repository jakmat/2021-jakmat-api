from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from src.classes.observations import perform_observation
from src.classes.observation import Observation

app = FastAPI()

origins = [
    "http://lab.jakubmatusiak.com",
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    #"http://localhost",
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"data": "home"}

@app.get("/test")
async def test():
    return {"data": "test"}

# @app.get("/observation")
@app.get("/observation", response_model=Observation)
async def planets_all(objects: Union[str], time: str, lat: str, lon: str):
    object_names = objects.split(",")
    observations = []
    for object in object_names:
        observable = perform_observation(object, time, lon, lat)
        observations.append(observable)
    response = jsonable_encoder(observations)
    return JSONResponse(content=response)