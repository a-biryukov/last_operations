import json


def load_file(filename) -> list:
    """
    Загружает список с данными из файла
    :param filename: Название файла с данными
    :return: Список с данными по операциям
    """
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)

    return data
