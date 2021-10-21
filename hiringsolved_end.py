import json
import requests


url = 'https://challenge.hiringsolved.com/038FD8'
name = 'Lee Pollok'
email = 'lee@pollok.io'
phone = '6026792805'
twitter = 'https://twitter.com/LeePollok'

final_url = '&'.join([
    url,
    'hirable=true',
    'name=' + name,
    'email=' + email,
    'phone=' + phone,
    'twitter=' + twitter])
print(final_url)
'''
response = requests.post(url, data=json.dumps(payload))
print(response)
print(response.text)
'''
