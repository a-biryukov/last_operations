from src.utils.functions import load_file, get_last_operations, enter_operations


def test_load_file(filename_fixture):
    assert type(load_file(filename_fixture)) == list


def test_get_last_operations(data_fixture, last_operations_fixture):
    assert get_last_operations(data_fixture) == last_operations_fixture


def test_enter_operations(last_operations_fixture, enter_fixture_1, enter_fixture_2, enter_fixture_3):
    assert enter_operations(last_operations_fixture[0]) == enter_fixture_1
    assert enter_operations(last_operations_fixture[1]) == enter_fixture_2
    assert enter_operations(last_operations_fixture[2]) == enter_fixture_3
