import requests
import json
from datetime import datetime
import os

API_KEY = f"{os.environ['API_KEY']}"
APP_ID = f"{os.environ['APP_ID']}"
TOKEN = f"{os.environ['TOKEN']}"
SHEETY_URL = f"{os.environ['SHEETY_URL']}"

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query = input("Tell me which exercises you did: ")

headers = {
    'x-app-id' : APP_ID,
    'x-app-key' : API_KEY
}

data = {
    "query": query
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
y = response.json()
print(y)

date = datetime.now()
time = datetime.now()

body = {
    'workout': {
        'date' : date.strftime("%d/%m/%Y"),
        'time' : time.strftime('%H:%M:%S'),
        'exercise' : y['exercises'][0]['name'],
        'duration' : y['exercises'][0]['duration_min'],
        'calories' : y['exercises'][0]['nf_calories']
    }
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': TOKEN
}


response = requests.post(url=SHEETY_URL, headers=headers, data=json.dumps(body))
print(response.text)
