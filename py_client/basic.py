import requests

base = "http://localhost:8000/api/"

response = requests.get(url=base)

print(response.json())
