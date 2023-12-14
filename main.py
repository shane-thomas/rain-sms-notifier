import requests

APIKEY = ''

#Al Manqaf, Kuwait
lat = 29.101179
lon = 48.131699

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APIKEY}&units=metric")
response.raise_for_status()
data = response.json()
print(data)