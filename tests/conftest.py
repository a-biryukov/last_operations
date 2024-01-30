import pytest
import os

filename = os.path.join("data", "operations.json")


@pytest.fixture
def filename_fixture():
    return filename
