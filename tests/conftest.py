import pytest
import os

filename = os.path.join("data", "operations.json")

basic_list = [
  {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
      "amount": "77751.04",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 27248529432547658655",
    "to": "Счет 84163357546688983493"
  },
  {
    "id": 615064591,
    "state": "EXECUTED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
      "amount": "77751.04",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 27248529432547658655",
    "to": "Счет 84163357546688983493"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
      "amount": "50870.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 4598300720424501",
    "to": "Visa Platinum 1246377376343588"
  },
  {},
  {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    }
]

executed_list = [
    {
        "id": 615064591,
        "state": "EXECUTED",
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {
            "amount": "77751.04",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 27248529432547658655",
        "to": "Счет 84163357546688983493"
    },
    {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
        "operationAmount": {
            "amount": "50870.71",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Maestro 4598300720424501",
        "to": "Visa Platinum 1246377376343588"
    },
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    }
]

sorted_list = [
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  },
  {
    "id": 615064591,
    "state": "EXECUTED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
        "amount": "77751.04",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 27248529432547658655",
    "to": "Счет 84163357546688983493"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
      "amount": "50870.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 4598300720424501",
    "to": "Visa Platinum 1246377376343588"
  }
]

enter_1 = """08.12.2019 Открытие вклада
Счет **5907
41096.24 USD
"""

enter_2 = """14.10.2018 Перевод со счета на счет
Счет **8655 -> Счет **3493
77751.04 руб.
"""

enter_3 = """26.01.2018 Перевод с карты на карту
Maestro 4598 30** **** 4501 -> Visa Platinum 1246 37** **** 3588
50870.71 руб.
"""


@pytest.fixture
def filename_fixture():
    return filename


@pytest.fixture
def basic_fixture():
    return basic_list.copy()


@pytest.fixture
def executed_fixture():
    return executed_list.copy()


@pytest.fixture
def sorted_fixture():
    return sorted_list.copy()


@pytest.fixture
def enter_fixture_1():
    return enter_1


@pytest.fixture
def enter_fixture_2():
    return enter_2


@pytest.fixture
def enter_fixture_3():
    return enter_3
