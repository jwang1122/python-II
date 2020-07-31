import requests
import json
response = json.loads(requests.get("http://localhost:5000/books").text)
print(response)