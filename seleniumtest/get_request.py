import requests


#url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get("https://jsonplaceholder.typicode.com/posts/10",timeout=15)
json_resp=response.json()
print(json_resp)

# print(json_resp)