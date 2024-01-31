from datetime import datetime, date
import json


def load_file(filename: str) -> list:
    """
    Загружает список с данными из файла
    :param filename: Название файла с данными и путь к нему
    :return: Список с данными по операциям
    """
    with open(filename, encoding="utf-8") as file:
        data_list = json.load(file)

    return data_list


def get_last_operations(data: list) -> list:
    """
    Удаляет из списка пустые словари, при их наличи
    Находит в списке последнюю по дате операцию, если она была отменена, то удаляет её из списка,
    если операция была выполнена, то удаляет её из списка и добавляет в новый список
    :param data: Список с операциями
    :return: Список с последними пятью операциями
    """
    while not all(data):
        data.remove({})

    last_operations = []

    while len(last_operations) < 5 and len(data) > 0:
        last_operation = max(
            data,
            key=lambda x: datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'))

        if last_operation["state"] == "EXECUTED":
            last_operations.append(data.pop(data.index(last_operation)))
        else:
            data.remove(last_operation)

    return last_operations


def enter_operations(operation: dict) -> str:
    """
    Выбирает нужную информацию об операции из словаря с данными и подготавливает её к выводу
    :param operation: Словарь с информацией об операции
    :return: Строка с нужной информацией об операции
    """
    the_date = date.fromisoformat(operation["date"].split("T")[0])
    date_formatted = the_date.strftime("%d.%m.%Y ")

    operation_name = operation["description"]

    amount = operation["operationAmount"]["amount"]

    currency = operation["operationAmount"]["currency"]["name"]

    from_to = []

    if "from" in operation.keys():
        lst = ["from", "to"]
    else:
        lst = ["to"]

    for i in lst:
        if len(operation[i].split()[-1]) == 16:
            from_to.append(f"{operation[i][:-12]} {operation[i][-12:-10]}** **** {operation[i][-4:]}")
        else:
            from_to.append(f"{operation[i][0:4]} **{operation[i][-4:]}")

    from_to = " -> ".join(from_to)

    return f"""{date_formatted}{operation_name}
{from_to}
{amount} {currency}
"""
