from datetime import datetime
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


def get_executed_operations(data: list) -> list:
    """
    Загружает файл с данными, выбирает выполненные операции и добавляет их в список,
    если в списке оказывается пустой словарь - пропускает его
    :param data: Список с данными по операциям
    :return: Список с выполненными операциями
    """
    executed_operations = []

    for operation in data:
        if not operation:
            continue
        elif operation["state"] == "EXECUTED":
            executed_operations.append(operation)

    return executed_operations


def sort_operations(executed_operations: list) -> list:
    """
    Сортирует операции по дате и возвращает последние пять
    :param executed_operations: Список с выполненными операциями
    :return: Список с последними пятью операциями
    """
    sorted_operations = sorted(
        executed_operations,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True
    )
    return sorted_operations[0:6]
