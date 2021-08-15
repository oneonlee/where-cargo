import requests
import json

datas = {
    'location' : '1',
    'state' : 'trucks' 
}
tmp = json.dumps(datas)
url = "http://165.246.241.118:8000/account/parking/"

print(type(tmp))
response = requests.post(url, data=tmp)
print(response.status_code)
print(response.request.body)