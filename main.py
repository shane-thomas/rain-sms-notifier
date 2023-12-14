import requests
from twilio.rest import Client
from creds import APIKEY, AUTH_TOKEN

ACCOUNT_SID = 'AC5c3cfc36fb9fcf3d0600858d89eac2b0'
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"


#Dandong
weather_params = {
    "lat": 40.000786,
    "lon": 124.354446,
    "units": "metric",
    "appid": APIKEY,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)


will_rain = False
weather_id = []
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id<700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
                .create(
                     body="It's going to rain, don't forget to get an umbrella!",
                     from_='+13312072671',
                     to='+918714410754'
                 ) 
    print("Bring Umbrella")

print(message.status)