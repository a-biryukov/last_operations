import os

from utils.functions import load_file, get_last_operations, enter_operations


def main():
    # Название файла с данными и путь к нему
    filename = os.path.join("..", "data", "operations.json")

    # Получение из файла списка с данными об операцих
    data_list = load_file(filename)

    # Получение последних пяти совершённых операций
    last_operations = get_last_operations(data_list)

    # Вывод последних пяти совершённых операций
    for num in range(5):
        print(enter_operations(last_operations[num]))


if __name__ == "__main__":
    main()
