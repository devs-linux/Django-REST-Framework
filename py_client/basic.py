import requests

base = "http://localhost:8000/api/"

response = requests.get(base)

print(response.json())
