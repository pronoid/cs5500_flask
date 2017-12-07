import requests
from json import dumps


UPSTREAM = 'http://flask-animaltracking.herokuapp.com'
ADMIN_DATA = dumps({"name": "admin", "password": "admin"})
ACCESS_TOKEN = {'content-type': 'application/json', 'token': 'x-access-token'}


# Just hit the endpoint
RESPONSE = requests.post(UPSTREAM, data=None)
assert RESPONSE.status_code == 405

# test admin
RESPONSE = requests.get(UPSTREAM, data=ADMIN_DATA, headers=ACCESS_TOKEN)
assert RESPONSE.status_code == 200

# test for getting all users
RESPONSE = requests.get(UPSTREAM+'/user', data=ADMIN_DATA, headers=ACCESS_TOKEN)
print(RESPONSE.json())

# same as above without admin data
RESPONSE = requests.get(UPSTREAM+'/user', data=ADMIN_DATA)
print(RESPONSE.json())
