import requests
URL = "https://namu.wiki/w/IVE?from=%EC%95%84%EC%9D%B4%EB%B8%8C"
response = requests.get(URL)
print(type(response))
print(dir(response))
print(response.text)
