from pydantic import BaseModel

class Observation(BaseModel):
    name: str
    azimuth: int
    altitude: int
    place: str
    time: str
