from flask import Flask, render_template, request, jsonify

from .python import parse_location_data


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

try:
    app.config.from_pyfile('config.py')
except:
    print("No instance specific config file found.")


# Homepage
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/location", methods=['GET', 'POST'])
def overland_listener():
    locations = request.get_json()
    parse_location_data(locations)
    return jsonify({"result": "ok"})
