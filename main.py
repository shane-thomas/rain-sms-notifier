import requests

APIKEY = ''
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"


#Al Manqaf, Kuwait


weather_params = {
    "lat": 29.101179,
    "lon": 48.131699,
    "units": "metric",
    "appid": APIKEY
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)