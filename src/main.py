import os

from utils.functions import load_file, get_executed_operations, sort_operations, enter_operations


def main():
    # Название файла с данными и путь к нему
    filename = os.path.join("..", "data", "operations.json")

    # Получение из файла списка с данными об операцих
    data = load_file(filename)

    # Получение списка с выполненными операциями
    executed_operations = get_executed_operations(data)

    # Сортировка списка по дате и выбор последних пяти операций
    sorted_operations = sort_operations(executed_operations)

    # Вывод последних пяти операций
    for num in range(5):
        print(enter_operations(sorted_operations[num]))


if __name__ == "__main__":
    main()
