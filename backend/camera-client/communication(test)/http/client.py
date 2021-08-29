import requests
import json

datas = {"0":1, "1":1, "2":1, "3":0}

tmp = json.dumps(datas)
url = "http://165.246.241.59:8000/account/parking/"

print(type(tmp))
response = requests.post(url, data=tmp)
print(response.status_code)
print(response.request.body)
print(response.headers)

