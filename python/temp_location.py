import json

temp_data = {
'lat':  37.788471914103894,
'lng':  -122.3873737062558,
'ts':   1535588778045,
'city':     "San Francisco",
'state':    "CA",
'country':  "United States",
}

with open('../json/location.json', 'w') as outfile:
    json.dump(temp_data, outfile)
