import requests
import pandas as pd

APP_ID = "333b3aaa983f6959e37a1890d9d90a987d43236d"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "LANG":"J",
    "statsDataId":"0004024800", #病院数，年次・都道府県別
    "cdArea": "1",
    
}

response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
