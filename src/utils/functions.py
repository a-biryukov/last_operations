from datetime import date
import json
import os


def load_file(filename: str) -> list:
    """
    Получает путь к файлу с данными
    Загружает список с данными из файла
    Удаляет из списка пустые словари, при их наличии
    :param filename: Название файла с данными
    :return: Список с данными по операциям
    """
    current_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
    file_path = os.path.join(parent_dir_path, "data", filename)

    with open(file_path, encoding="utf-8") as file:
        data_list = json.load(file)

    while not all(data_list):
        data_list.remove({})

    return data_list


def get_last_operations(data: list) -> list:
    """
    Находит в списке последнюю по дате операцию, если она была отменена, то удаляет её из списка,
    если операция была выполнена, то удаляет её из списка и добавляет в новый список
    :param data: Список с операциями
    :return: Список с последними пятью операциями
    """

    last_operations = []

    while len(last_operations) < 5 and len(data) > 0:
        last_operation = max(data, key=lambda x: x["date"])

        if last_operation.get("state") == "EXECUTED":
            last_operations.append(data.pop(data.index(last_operation)))
        else:
            data.remove(last_operation)

    return last_operations


def get_operation_information(operation: dict) -> str:
    """
    Выбирает нужную информацию об операции из словаря с данными и подготавливает её к выводу
    :param operation: Словарь с информацией об операции
    :return: Строка с нужной информацией об операции
    """
    the_date = date.fromisoformat(operation.get("date").split("T")[0])
    date_formatted = the_date.strftime("%d.%m.%Y ")

    operation_name = operation.get("description")

    amount = operation.get("operationAmount").get("amount")

    currency = operation.get("operationAmount").get("currency").get("name")

    from_to = []

    if "from" in operation.keys():
        lst = ["from", "to"]
    else:
        lst = ["to"]

    for i in lst:
        if len(operation.get(i).split()[-1]) == 16:
            from_to.append(f"{operation[i][:-12]} {operation[i][-12:-10]}** **** {operation[i][-4:]}")
        else:
            from_to.append(f"{operation[i][0:4]} **{operation[i][-4:]}")

    from_to = " -> ".join(from_to)

    operation_information = f"""{date_formatted}{operation_name}
{from_to}
{amount} {currency}
"""

    return operation_information
