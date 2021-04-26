import json
import requests

url = "http://127.0.0.1:8000/stuadd/"


data = {
    'name': 'dummy',
    'roll': 100,
    'city': 'berkeley'
}

json_data = json.dumps(data)

r = requests.post(url=url, data=json_data)
data = r.json()
print(data)
