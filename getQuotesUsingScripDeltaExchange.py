# prompt: write a python code for delta exchange india to find out the ltp for C-BTC-50000-300824

import requests
import hashlib
import hmac
import json
import time

api_key = "doesnotmatter"
api_secret = "same as above"

url = "https://cdn.india.deltaex.org/v2/tickers/C-BTC-55600-090724"

headers = {
    "X-API-KEY": api_key,
    "X-API-SECRET": api_secret,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    ticker = response.json()
    # Print the ltp
    print(ticker)
    #print(ticker['ltp'])
else:
    print("Error:", response.status_code)
