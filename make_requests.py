

import requests

# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.json())

# 'Authorization': 'Bearer{access_token}'

my_headers = {'token': 'OMotlQeFKcGYHHhqufQiZrRKDqBeSxLS',
              'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate, br',
              'Connection': 'keep-alive',
              'Content-Type': 'application/json'
              }

response = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset={offset}&limit=1000', headers=my_headers)

data = response.json()

with open