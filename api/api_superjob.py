import json
from abc import ABC, abstractmethod
from pprint import pprint

import os
import requests
import dotenv

dotenv.load_dotenv()


class API(ABC):
    @abstractmethod
    def get_response(self, search_keyword):
        raise NotImplemented


class SuperJobAPI(API):
    api_key: str | None = os.environ.get("API_KEY_SUPERJOB")

    def __init__(self):
        self.search_keyword = None
        self.headers = {
            "X-Api-App-Id": self.api_key}
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_response(self, search_keyword="python"):
        self.search_keyword = search_keyword
        params = {
            "keyword": self.search_keyword
        }
        response = requests.get(self.url, params=params, headers=self.headers)
        if response.status_code == 200:
            return response.json().get("objects", [])
        else:
            print(f"Ошибка {response.status_code}")
            return []


# s = SuperJobAPI()
# slovo = s.get_response()
# pprint(slovo)
# pprint(slovo['objects'][0]['link'])
# pprint(slovo['objects'][0]['candidat'])
# pprint(slovo['objects'][0]['payment_from'])
# pprint(slovo['objects'][0]['profession']) # название вакансии
# for i in slovo['objects']:
#     print(i['profession'])
