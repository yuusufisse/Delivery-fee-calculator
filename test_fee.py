import json
import requests

payload = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2023-02-03T13:00:00Z"}
response = requests.post("http://127.0.0.1:5000/delivery_fee", json=payload)
print(response.json())