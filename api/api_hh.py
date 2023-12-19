from pprint import pprint

import requests

from api.api_superjob import API


class HeadHunterAPI(API):
    """
    API поиска работы HeadHunter.
    """

    def __init__(self):
        """
        Конструктор класса HeadHunterAPI.
        Устанавливает базовый URL и заголовки для запросов к API HeadHunter.
        """
        self.base_url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def get_response(self, search_keyword):
        url = f"{self.base_url}"
        params = {"text": search_keyword}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:

            return response.json().get("items", [])
        else:
            print(
                f"Failed to retrieve vacancies from HeadHunter. Status code: {response.status_code}"
            )
            return []


probe = HeadHunterAPI()
pprint(probe.get_response("python"))