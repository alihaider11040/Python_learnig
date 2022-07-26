import requests
import sys
import json

response = requests.get('https://itunes.apple.com/search?entity=songs&limit=1&term=weezer')

o = response.json()
for result in o["results"]:
    print(result["trackName"])