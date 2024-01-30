from src.utils.functions import load_file, get_executed_operations, sort_operations


def test_load_file(filename_fixture):
    assert type(load_file(filename_fixture)) == list


def test_get_executed_operations(basic_fixture, executed_fixture):
    assert get_executed_operations(basic_fixture) == executed_fixture


def test_sort_operations(executed_fixture, sorted_fixture):
    assert sort_operations(executed_fixture) == sorted_fixture
