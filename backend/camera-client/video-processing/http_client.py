import requests
import json


def http_client(datas, url):
    tmp = json.dumps(datas)
    requests.post(url, data=tmp)

# print(type(tmp))
# print(response.status_code)
# print(response.request.body)
# print(response.headers)
