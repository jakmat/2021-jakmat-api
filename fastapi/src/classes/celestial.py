from string import Template
from skyfield.api import load

class Celestial:
    def __init__(self, name):
        self.name = name
        self.caption = name.capitalize()
        self.set_object()

    def set_object(self):
       planets = load('de421.bsp')
       self.object = planets[self.name]

    def observe(self, location, time):
        astrometric = location.position.at(time.astrometric_dt).observe(self.object).apparent()
        obj_name = self.caption
        loc_lon = location.lon
        loc_lat = location.lat
        alt, az, distance = astrometric.altaz()
        tm = time.local_dt
        observation = Template(
            'Observing ${obj_name} for location ${loc_lon}/{loc_lat} at time $tm: * azimuth: ${az} | * altitude: ${alt}').substitute(
            obj_name=obj_name, loc_lon=loc_lon, loc_lat=loc_lat, tm=tm, az=az, alt=alt)

    def get_observation(self, location, time):
        astrometric = location.position.at(time.astrometric_dt).observe(self.object).apparent()
        obj_name = self.caption
        alt, az, distance = astrometric.altaz()
        tm = time.local_dt
        observation = {
            'objective': obj_name,
            'azimuth': az.degrees,
            'altitude': alt.degrees,
            'time': tm.strftime("%d.%m.%Y, %H:%M")
        }
        return observation