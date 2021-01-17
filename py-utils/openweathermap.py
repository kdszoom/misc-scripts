import requests
import json
from datetime import datetime

# Use api https://openweathermap.org/api/one-call-api
# Get Location params
# http://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&APPID={api-key}

API_KEY = "{your-api-key}"
LOT = "37.6156"
LAT = "55.7522"
EXCLUDE_PART = "minutely,hourly,alerts"

QUERY = f'units=metric&lat={LAT}&lon={LOT}&exclude={EXCLUDE_PART}&appid={API_KEY}'
URL = f'https://api.openweathermap.org/data/2.5/onecall?{QUERY}'

response = requests.get(URL)

if response.status_code == 200:
	forecast = json.loads(response.text)
	daily_slice = forecast['daily'][1:5]
	max_morn_temp = forecast['daily'][0]['temp']['morn']
	dt = forecast['daily'][0]['dt']
	for day in daily_slice:
		if day['temp']['morn'] > max_morn_temp:
			max_morn_temp = day['temp']['morn']
			dt = day['dt']
	print("Maximum morn temp for the next 5 days {} at {}".format(max_morn_temp, datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')))
else:
	exit(1)
