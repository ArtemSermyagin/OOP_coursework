import json
from abc import ABC, abstractmethod

from api.api_superjob import SuperJobAPI

s = SuperJobAPI()
json_data = s.get_response()


# print(json_data)

class Vacancies:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{self.title}\n{self.link}\n{self.salary}\n{self.description}"

    def __eq__(self, other: int) -> bool:
        """
        Сравнивает значение атрибута salary текущего объекта
        со значением атрибута salary другого объекта
        :param other: int
        :return: bool
        """
        return self.salary == other.salary

    def __lt__(self, other: int) -> bool:
        """
        Сравнивает значение атрибута salary текущего объекта со значением
        атрибута salary другого объекта. Если значение атрибута
        salary текущего объекта меньше значения атрибута salary другого объекта
        :param other: int
        :return: bool
        """
        return self.salary < other.salary


    def validate_data(self):
        pass


class SaveJsonABC(ABC):
    @abstractmethod
    def add_job(self, job):
        """
        Абстрактный метод для добавления вакансии
        :param job: Вакансия для добавления
        :return: bool
        """
        raise NotImplemented

    @abstractmethod
    def get_jobs(self, criteria):
        """
        Абстрактный метод для получения списка вакансий по заданным критериям
        :param criteria: фильтр
        :return: list
        """
        raise NotImplemented

    @abstractmethod
    def delete_jobs(self, criteria):
        """
        Абстрактный метод для удаления вакансии
        :param criteria: Вакансия
        :return: bool
        """
        raise NotImplemented

class SaveJson(SaveJsonABC):

    def to_json(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.__dict__, f, indent=4, ensure_ascii=False)
