import requests
# if requests package is not installed in the path execute the following command
# python -m pip install requests
response = requests.api.get('http://api.open-notify.org/astros.json')
json = response.json()
# print(json)

for person in json.get("people"):
    print(person['name'])