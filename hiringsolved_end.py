import json
import requests


url = 'https://challenge.hiringsolved.com/038FD8'
payload = {'hirable': 'true',
           'name': 'Lee Pollok',
           'email': 'lee.pollok@gmail.com',
           'phone': '6026792805',
           'twitter': 'https://twitter.com/LeePollok'}
response = requests.post(url, data=json.dumps(payload))
print(response)
print(response.text)

