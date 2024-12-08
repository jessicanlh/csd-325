import requests
import json
response = requests.get("https://ssd-api.jpl.nasa.gov/fireball.api?limit=20")
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())

