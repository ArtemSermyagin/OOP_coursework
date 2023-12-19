import json

from api.api_superjob import SuperJobAPI

s = SuperJobAPI()
json_data = s.get_response()


# print(json_data)

class SuperJob:
    def __init__(self, data):
        self.data = data['objects'][0]
        self.title = self.data['profession']  # название вакансии
        self.description = self.data['candidat']
        self.salary = self.data['payment_from']
        self.url = self.data['link']

    def __str__(self):
        return f"{self.title}\n{self.url}\n{self.salary}\n{self.description}"
    #
    # def __eq__(self, other):
    #     return self.salary == other.salary
    #
    # def __lt__(self, other):
    #     return self.salary < other.salary
    #
    # def validate_data(self):
    #     pass
# Ваш код для валидации данных атрибутов вакансии
    def to_json(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.__dict__, f, indent=4, ensure_ascii=False)

s_s = SuperJob()
at = s_s.__init__(json_data)
print(at)
