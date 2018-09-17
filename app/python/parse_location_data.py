import json

from .reverse_geocode import reverse_geocode


def parse_location_data(data):
    latest_coors = data["locations"][0]["geometry"]["coordinates"]
    ts = data["locations"][0]["properties"]["timestamp"]
    # print(latest_coors)
    # print(ts)
    write_location_to_json(latest_coors, ts)


def write_location_to_json(coors, timestamp):
    city, state, country = reverse_geocode(coors)

    data = {
    'lat':      coors[1],
    'lng':      coors[0],
    'ts':       timestamp,
    'city':     city,
    'state':    state,
    'country':  country
    }
    print(data)

    with open('app/static/json/location.json', 'w') as outfile:
        json.dump(data, outfile)
