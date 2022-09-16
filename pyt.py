import requests
url="https://api.zalando.com/articles"
response_code=requests.get(url+"/articles")
print(response_code)
