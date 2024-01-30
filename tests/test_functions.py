from src.utils.functions import load_file, get_executed_operations, sort_operations, enter_operations


def test_load_file(filename_fixture):
    assert type(load_file(filename_fixture)) == list


def test_get_executed_operations(basic_fixture, executed_fixture):
    assert get_executed_operations(basic_fixture) == executed_fixture


def test_sort_operations(executed_fixture, sorted_fixture):
    assert sort_operations(executed_fixture) == sorted_fixture


def test_enter_operations(sorted_fixture, enter_fixture_1, enter_fixture_2, enter_fixture_3):
    assert enter_operations(sorted_fixture[0]) == enter_fixture_1
    assert enter_operations(sorted_fixture[1]) == enter_fixture_2
    assert enter_operations(sorted_fixture[2]) == enter_fixture_3
