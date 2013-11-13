def get_geolocation(result):
    address = ["", "", "", ""]
    for obj in result["address_components"]:
        if "locality" in obj["types"]:
            address[0] = obj["long_name"]
        if "administrative_area_level_1" in obj["types"]:
            address[1] = obj["long_name"]
        if "country" in obj["types"]:
            address[2] = obj["long_name"]
    return  tuple(address)

import requests
import json

url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=40,-76&sensor=false"
print get_geolocation(json.loads(requests.get(url).text)["results"][0])
url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=50,13&sensor=false"
print get_geolocation(json.loads(requests.get(url).text)["results"][0])