from datetime import datetime, date
import json


def load_file(filename) -> list:
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
    Находит в списке последнюю по дате выполненную операцию и добавляет её в новый список
    :param data: Список с операциями
    :return: Список с последними пятью операциями
    """
    while not all(data):
        data.remove({})

    last_operations = []

    while len(last_operations) < 5:
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
    # Форматирование даты
    the_date = date.fromisoformat(operation["date"].split("T")[0])
    date_formatted = the_date.strftime("%d.%m.%Y ")

    # Строка с информацией куда сделан перевод (карта или счет)
    to_ = operation["to"].split()
    if len(to_[-1]) == 16:
        operation_to = f"{operation["to"][:-12]} {operation["to"][-12:-10]}** **** {operation["to"][-4:]}"
    else:
        operation_to = f"{operation["to"][0:5]}**{operation["to"][-4:]}"

    # Строка с информацией откуда сделан перевод (карта или счет)
    if "from" in operation.keys():
        from_ = operation["from"].split()
        if len(from_[-1]) == 16:
            operation_from = f"{operation["from"][:-12]} {operation["from"][-12:-10]}** **** {operation["from"][-4:]}"
        else:
            operation_from = f"{operation["from"][0:5]}**{operation["from"][-4:]}"

    # Объединение строк откуда и куда сделан перевод (если открытие вклада - только номер счета)
        from_to = f"{operation_from} -> {operation_to}"
    else:
        from_to = operation_to

    return f"""{date_formatted}{operation["description"]}
{from_to}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}
"""
