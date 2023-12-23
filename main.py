from api.api_hh import HeadHunterAPI
from api.api_superjob import SuperJobAPI
from utils.sort_utils import filter_vacancies, sort_vacancies, number_of_vacancies, print_vacancies
from utils.utils import SaveJson, Vacancies

if __name__ == "__main__":
    api_hh = HeadHunterAPI()
    api_superjob = SuperJobAPI()
    json_saver = SaveJson("vacancies.json")

    api_hh.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                    ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Получение вакансий с разных платформ
    hh_vacancies = api_hh.get_response("Python")
    superjob_vacancies = api_superjob.get_response("Python")

    # # Создание вакансий для примера
    # vacancy1 = Vacancies(
    #     "Python Developer",
    #     "https://hh.ru/vacancy/123456",
    #     "100 000-150 000 руб.",
    #     "Требования: опыт работы от 3 лет...",
    # )
    # vacancy2 = Vacancies(
    #     "Data Scientist",
    #     "https://superjob.ru/vacancy/789012",
    #     "120 000-160 000 руб.",
    #     "Требования: знание Python, опыт с ML...",
    # )
    #
    # # Сохранение вакансий в файл
    # json_saver.add_job(vacancy1)
    # json_saver.add_job(vacancy2)

    # Взаимодействие с пользователем
    print("Доступные платформы: HeadHunter, SuperJob")

    # Выбор платформы
    platform = input("Выберите платформу (HeadHunter/SuperJob): ").lower()

    if platform not in ["headhunter", "superjob"]:
        print("Некорректная платформа. Выход из программы.")

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_words = input(
        "Введите ключевые слова для фильтрации вакансий (через пробел): "
    ).split()

    # Получение вакансий с выбранной платформы
    platform_vacancies = (
        hh_vacancies if platform == "headhunter" else superjob_vacancies
    )

    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(platform_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")

    # Сортировка вакансий
    sorted_vacancies = sort_vacancies(filtered_vacancies)

    # Получение топ-N вакансий
    top_vacancies = number_of_vacancies(sorted_vacancies, top_n)

    # Вывод вакансий в консоль
    print("Результаты поиска:")
    print_vacancies(top_vacancies)

    # Спросить пользователя, хочет ли он сохранить найденные вакансии
    save_choice = input("Хотите сохранить найденные вакансии? (да/нет): ").lower()
    if save_choice == "да":
        for vacancy in top_vacancies:
            json_saver.add_job(vacancy)
