# -*- coding: UTF-8 -*-
import requests

def get_req(url: str, token: str, **kwargs) -> dict:
    result = {}

    # request header
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json; charset=utf-8'
    }

    # method get request
    response = requests.request(
        method="GET",
        url=url,
        params=kwargs,
        headers=headers
    )

    # response
    if response.status_code == 200:
        result = response.json()
    return result

 

if __name__ == '__main__':
    url = "https://xxx.xxx.xx/xxx/xxx/"
    token = "Token xxxxxxxxxxxxxx"
    query_params = {
        'username': "xxxxxx"
    }
    res = get_req(url=url, token=token, **query_params)
    if res:
        print(res.get("xxx"))
