from src.classes.celestial import Celestial
from src.classes.location import Location
from src.classes.date_time import DateTime

def perform_observation(object, timestamp, longitude, latitude):
    # for observable in observables:
    celestial = Celestial(object)
    place = Location(longitude, latitude)
    time = DateTime(timestamp)
    efemeride = celestial.get_observation(place, time)
    return efemeride
