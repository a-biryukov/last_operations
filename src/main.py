from utils.functions import load_file, get_last_operations, get_operation_information


def main():
    # Название файла с данными
    filename = "operations.json"

    # Получение из файла списка с данными об операциях
    data_list = load_file(filename)

    # Получение последних пяти совершённых операций
    last_operations = get_last_operations(data_list)

    # Вывод последних пяти совершённых операций
    for num in range(len(last_operations)):
        print(get_operation_information(last_operations[num]))


if __name__ == "__main__":
    main()
