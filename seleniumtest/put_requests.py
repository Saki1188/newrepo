import requests
import json
payload = {"userId": 1,
  "id": 1,
  "title": "sak",
  "body": "saki testing"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1",data=payload)
print(response.json())
print(response)