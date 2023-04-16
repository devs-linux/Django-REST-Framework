import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Cats Video"
}

response = requests.post(url=endpoint, data=data)

print(response.text)
