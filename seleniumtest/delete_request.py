import requests

resp=requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(resp.status_code)
