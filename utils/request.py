from dataclasses import dataclass

import requests

class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict
    
    def __init__(self, status_code, text, as_dict, headers):
        self.status_code = status_code
        self.text = text
        self.as_dict = as_dict
        self.headers = headers
    
class APIRequest:
    def get(self, url, headers):
        response = requests.get(url, headers=headers)
        return self.__get_responses(response)
    
    def post(self, url, payload, headers):
        response = requests.post(url=url, data=payload, headers=headers)
        return self.__get_responses(response)
    
    def put(self, url, payload, headers):
        response = requests.put(url=url, data=payload, headers=headers)
        return self.__get_responses(response)
    
    def patch(self, url, payload, headers):
        response = requests.patch(url=url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, url, headers):
        response = requests.delete(url=url, headers=headers)
        return self.__get_responses(response)
    
    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )        