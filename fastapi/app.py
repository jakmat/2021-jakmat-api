from fastapi import FastAPI
from typing import Union
from src.classes.observations import perform_observation
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/observation")
async def planets_all(objects: Union[str, None], time: str, lat: str, lon: str):
    #objects = request.args.get('objects')
    object_names = objects.split(",")
    #timestamp = request.args.get('time')
    #latitude = request.args.get('lat')
    #longitude = request.args.get('lon')
    observations = []
    for object in object_names:
        observable = perform_observation(object, time, lon, lat)
        observations.append(observable)
    return observations
