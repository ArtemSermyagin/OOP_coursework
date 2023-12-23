def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате
    :param vacancies: List[dict]
    :return: List[dict]
    """
    return sorted(vacancies, key=lambda x: x.salary)


def number_of_vacancies(vacancies, n):
    """
    Возвращает заданное количество вакансий.
    :param vacancies: List[dict]
    :param n: int
    :return: List[dict]
    """
    return vacancies[:n]


def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях в консоль.
    :param vacancies: List[dict]
    :return: dict
    """
    for vacancy in vacancies:
        print(vacancy)


def filter_vacancies(vacancies, filter_words):
    filtered_vacancies = []
    for vacancy in vacancies:
        if all(word.lower() in vacancy.description.lower() for word in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies
