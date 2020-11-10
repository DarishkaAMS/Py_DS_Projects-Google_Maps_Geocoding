import requests
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl

# https://console.cloud.google.com/apis/credentials?authuser=1&project=cfe-project-295104
api_key = "AIzaSyD31cVxW6IO9JOsvia_Eu96lRSKuFRzzxE"

data_type = "json"
endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
params = {'adress': "1600 Amphitheatre Parkway, Mountain+View, CA", "key": api_key}
# https://developers.google.com/maps/documentation/geocoding/start
url_params = urlencode(params)
# sample = "https://maps.googleapis.com/maps/api/geocode/json?" \
#          "address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"
# print(url_params)

url = f"{endpoint}?{url_params}"
# print(url)


def extract_lat_lng(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")

# extract_lat_len("1600 Amphitheatre Parkway, Mountain+View, CA")


to_parse = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,' \
           '+CA&key=YOUR_API_KEY '
urlparse(to_parse)
parsed_url = urlparse(to_parse)
query_str = parsed_url.query
query_tuple = parse_qsl(query_str)
query_dict = dict(query_tuple)

endpoint = f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}'

lat, lng = 37.42230960000001, -122.0846244
base_endpoint_places = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
params = {
    'key': api_key,
    'input': 'Italian Food',
    'input_type': 'textquery',
    'fields': 'address_component,name,geometry, permanently_closed'
}
locationbias = f'point:{lat},{lng}'
use_circular = False
if use_circular:
    radius = 1000
    locationbias = f'circle:{radius}@{lat},{lng}'
params['locationbias']: locationbias

params_encoded = urlencode(params)
places_endpoint = f'{base_endpoint_places}?{params_encoded}'
# print(places_endpoint)

r = requests.get(places_endpoint)
print(r.status_code)
r.json()