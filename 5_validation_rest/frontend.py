import requests
import json

url = "http://127.0.0.1:8000/student_api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)


# get_data()  # for read operation


def post_data():
    data = {'name': 'ravi',
            'roll': 10, 'city': 'vegas'}
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)


# post_data()  # adding data


def update_data():
    data = {
        'id': 6,
        'name': 'swapnil',
        'roll': 3,
        'city': 'nanded'}
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)


update_data()  # updating data


def delete_data():
    data = {
        'id': 3,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)


# delete_data()  # delete
