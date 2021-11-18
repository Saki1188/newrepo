import requests
import json
#url = ("https://jsonplaceholder.typicode.com/posts",data=payload)
mydata=open("data.json","r").read()
response = requests.post("https://jsonplaceholder.typicode.com/posts",data=json.loads(mydata))
print(response)
print(response.json())
#assert response.json()['title']=='suntjaffa'