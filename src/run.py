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
    object = request.args.get('object')
    timestamp = request.args.get('time')
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    observable = perform_observation(object, timestamp, longitude, latitude)
    observation = jsonify(observable)
    return observation

if __name__ == "__main__":
    app.run()
