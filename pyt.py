import requests
url="https://api.zalando.com/articles"
response_code=requests.get(url+"/articles")
print(response_code)
r = requests.get('https://api.github.com/events')
r=requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
