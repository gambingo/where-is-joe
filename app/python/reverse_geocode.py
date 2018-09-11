import os
import googlemaps


def reverse_geocode(coordinates):
    api_key = os.environ["GMAPS_KEY"]
    gmaps = googlemaps.Client(key=api_key)
    coordinates = (coordinates[1], coordinates[0])
    reverse_geocode_result = gmaps.reverse_geocode(tuple(coordinates))
    # print(reverse_geocode_result)

    for component in reverse_geocode_result[0]["address_components"]:
        if "locality" in component["types"]:
            city = component["long_name"]

        if "administrative_area_level_1" in component["types"]:
            state = component["short_name"]

        if "country" in component["types"]:
            country = component["long_name"]

    print("city: ", city)
    print("state: ", state)
    print("country: ", country)

    return city, state, country


if __name__ == "__main__":
    coors = [-122.14678061069175, 37.42834085786257]
    city, state, country = reverse_geocode(coors)
