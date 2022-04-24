from classes.celestial import Celestial
from classes.location import Location
from classes.date_time import DateTime

def perform_observation(object, timestamp, longitude, latitude):
    # for observable in observables:
    celestial = Celestial(object)
    place = Location(longitude, latitude)
    time = DateTime(timestamp)
    efemeride = celestial.get_observation(place, time)
    observation = {
        'efemeride': efemeride,
        'object': object,
        'timestamp': timestamp,
        'latitude': latitude,
        'longitude': longitude
    }
    return observation
