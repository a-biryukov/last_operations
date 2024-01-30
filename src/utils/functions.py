from datetime import datetime, date
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
