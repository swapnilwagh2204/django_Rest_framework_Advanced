import requests

url = "http://127.0.0.1:8000/stulist/"

data = requests.get(url=url)

data_in_json = data.json()

print(data_in_json)
