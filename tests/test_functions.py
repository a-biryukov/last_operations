from src.utils.functions import load_file


def test_load_file(filename_fixture):
    assert type(load_file(filename_fixture)) == list

