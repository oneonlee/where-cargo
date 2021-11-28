import requests
import json


def http_client(datas, url):
    tmp = json.dumps(datas)
    requests.post(url, data=tmp)
    # print(requests.post(url, data=tmp))
    # print(requests.post(url, data=tmp).status_code)
    # print(requests.post(url, data=tmp).headers)
    # print(requests.post(url, data=tmp).request.body)


# print(type(tmp))
# print(response.request.body)
# print(response.headers)

# test
url = "http://158.247.202.164/result/"
datas = {0: 1, 1: 0, 2: 1, 3: 0, 4: 0, 5: 1, 6: 0, 7: 0}

http_client(datas, url)
