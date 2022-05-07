from flask import Flask, jsonify, request
from classes.observations import perform_observation
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/test": { "origins": "http://localhost:3000" }})
# cors = CORS(app, resources={r"/test": { "origins": "http://172.19.0.3:3000" }})

@app.route('/test')
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def test_api():
    response = jsonify(data="This is a test...")
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response

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
