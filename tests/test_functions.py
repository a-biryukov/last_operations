from src.utils.functions import load_file, get_executed_operations


def test_load_file(filename_fixture):
    assert type(load_file(filename_fixture)) == list


def test_get_executed_operations(array_fixture, executed_fixture):
    assert get_executed_operations(array_fixture) == executed_fixture