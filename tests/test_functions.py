from src.utils.functions import load_file, get_last_operations, get_operations_information


def test_load_file(filename_fixture):
    assert type(load_file(filename_fixture)) == list


def test_get_last_operations(data_fixture, last_operations_fixture):
    assert get_last_operations(data_fixture) == last_operations_fixture


def test_get_information_operations(last_operations_fixture, info_fixture_1, info_fixture_2, info_fixture_3):
    assert get_operations_information(last_operations_fixture[0]) == info_fixture_1
    assert get_operations_information(last_operations_fixture[1]) == info_fixture_2
    assert get_operations_information(last_operations_fixture[2]) == info_fixture_3
