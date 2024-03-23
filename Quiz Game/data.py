import requests
import json

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_data = response.json()


# Save the data to a JSON file
with open('question_data.json', 'w') as f:
    json.dump(question_data, f)

