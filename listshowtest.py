import requests
import json

url = 'http://localhost:8000/list/'
response = requests.get(url)

print(response.status_code)
print(json.dumps(response.json(), ensure_ascii=False, indent=4))