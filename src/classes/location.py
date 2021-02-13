from skyfield import api

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.set_position()

    def set_position(self):
        planets = api.load('de421.bsp')
        earth = planets['earth']
        self.position = earth + api.Topos(self.longitude, self.latitude)