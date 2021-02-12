from flask import Flask, request, jsonify
# from observations import perform_observation
from flask_cors import CORS
from datetime import date

app = Flask(__name__)
CORS(app)

@app.route('/test')
def test_api():
    return jsonify(data="This is a test")

# @app.route('/celestial-objects')
# def planets_all():
#     object = request.args.get('object')
#     timestamp = request.args.get('time')
#     print(object)
#     print(timestamp)
#     # lon = request.args.get('lon')
#     # lat = request.args.get('lat')
#     observable = perform_observation(object, timestamp)
#     observation = jsonify(observable)
#     return observation

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
