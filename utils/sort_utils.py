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


def filter_vacancies(vacancies, filter_words): # перенести в класс вакансий
    filtered_vacancies = []
    for vacancy in vacancies:
        for filter_word in filter_words:
            if filter_word in vacancy.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies
