#! /usr/bin/env python3
import requests
import json
import webbrowser

request_headers = {
  'User-agent': 'Shower thoughts bot'
}

response = requests.get('https://api.reddit.com/r/funny', headers=request_headers)
response_json = response.json()
# Uncomment for debugging
# print(json.dumps(response_json, indent=2))
opened_links = 0
for entry in response_json['data']['children']:
    if opened_links >= 5:
        break
    webbrowser.open(entry['data']['url'])
    opened_links += 1

