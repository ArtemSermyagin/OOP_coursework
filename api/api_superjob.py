import json
from abc import ABC, abstractmethod
from pprint import pprint

import os
import requests
import dotenv

dotenv.load_dotenv()


class API(ABC):
    @abstractmethod
    def get_response(self):
        raise NotImplemented


class SuperJobAPI(API):
    api_key: str | None = os.environ.get("API_KEY_SUPERJOB")

    def __init__(self, keyword="python"):
        self.headers = {
            "X-Api-App-Id": self.api_key}
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.keyword = keyword
        self.params = {
            "keyword": self.keyword
        }

    def get_response(self):
        response = requests.get(self.url, params=self.params, headers=self.headers).json()
        # json_data = json.dumps(response, indent=4, ensure_ascii=False)
        return response


# s = SuperJobAPI()
# slovo = s.get_response()
# pprint(slovo['objects'][0])
# pprint(slovo['objects'][0]['link'])
# pprint(slovo['objects'][0]['candidat'])
# pprint(slovo['objects'][0]['payment_from'])
# pprint(slovo['objects'][0]['profession']) # название вакансии
# for i in slovo['objects']:
#     print(i['profession'])


