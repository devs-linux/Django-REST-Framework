import requests
import sys

args = sys.argv
id = args[1] if len(args) > 1 else 1

endpoint = f"http://localhost:8000/api/products/{id}/update/"
data = {
    "title": "Updated"
}

response = requests.put(url=endpoint, data=data)

print(response.text)
