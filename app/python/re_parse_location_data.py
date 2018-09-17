import json

from .parse_location_data import write_location_to_json


def call_gmaps():
    with open("app/static/json/location.json") as f:
        data = json.load(f)

    try data["state"]:
        pass
    except KeyError:
        coordinates = (data["lng"], data["lat"])
        print(coordinates)
        write_location_to_json(coordinates, "")
