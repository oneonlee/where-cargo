print(requests.post(url, data=tmp))
    print(requests.post(url, data=tmp).status_code)
    print(requests.post(url, data=tmp).headers)
    print(requests.post(url, data=tmp).request.body)
