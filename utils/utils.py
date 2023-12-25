import json
from abc import ABC, abstractmethod

from api.api_superjob import SuperJobAPI

s = SuperJobAPI()
json_data = s.get_response()


# print(json_data)

class Vacancies:
    def __init__(self, title, link, salary):
        self.title = title
        self.link = link
        self.salary = salary
        self.validate_data()

    def __str__(self):
        return f"{self.title}\n{self.salary}"

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
        if self.salary and isinstance(self.salary, dict):
            from_ = self.salary.get("from")
            to = self.salary.get("to")
            self.salary["from"] = from_ if from_ else 0
            self.salary["to"] = to if to else 0
        else:
            self.salary = {
                "from": 0,
                "to": 0,
            }



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
    def __init__(self, file_name="vacancies.json"):
        self.file_name = file_name
        self.vacancies = []

    def add_job(self, job):
        self.vacancies.append(job)
        self.to_json()
        print(f"Вакансия записана в {self.file_name}")

    def get_jobs(self, criteria):
        return [
            Vacancies(**vacancy)
            for vacancy in self.vacancies
            if all(vacancy.get(key) == value for key, value in criteria.items())
        ]

    def delete_jobs(self, criteria):
        vacancy_data = vars(criteria)
        if vacancy_data in self.vacancies:
            self.vacancies.remove(vacancy_data)
            self.to_json()
            return True
        return False

    def to_json(self):
        with open(self.file_name, "w") as f:
            json.dump(self.vacancies, f, indent=4, ensure_ascii=False)
