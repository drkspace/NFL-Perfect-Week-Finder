import requests

url = "https://api.nfl.com/v1/scores"

parameters = {
    "week.season": 2017, 
    "week.seasonType": "POST", 
    "week.week": 1
  }

responce = requests.get(url, params = parameters)
print(responce.content)