from flask import Flask, jsonify, request
from classes.observations import perform_observation
#from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route('/test')
def test_api():
    return jsonify(data="This is a test")

@app.route('/observation')
def planets_all():
    objects = request.args.get('objects')
    object_names = objects.split(",")
    timestamp = request.args.get('time')
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    observables = []
    for object in object_names:
        observable = perform_observation(object, timestamp, longitude, latitude)
        observables.append(observable)
    observations = jsonify(observables)
    return observations
# test: http://172.17.0.2:5000/observation?objects=sun,mercury,venus,moon,mars,jupiter_barycenter,saturn_barycenter,uranus_barycenter,neptune_barycenter,pluto_barycenter&time=1650773000&lat=52n&lon=19e

if __name__ == "__main__":
    app.run()
