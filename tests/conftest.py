import pytest
import os

filename = os.path.join("data", "operations.json")

data_list = [
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
    "from": "Visa Classic 4062745111784804",
    "to": "Maestro 8602249654751155"
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
  },
  {
    "id": 232222017,
    "state": "EXECUTED",
    "date": "2018-07-06T22:32:10.495465",
    "operationAmount": {
        "amount": "37160.27",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 23177857685058835559",
    "to": "Счет 56363465303962313778"
  },
  {
    "id": 280743947,
    "state": "EXECUTED",
    "date": "2018-09-27T14:26:24.629306",
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
]


last_operations = [
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
    "id": 280743947,
    "state": "EXECUTED",
    "date": "2018-09-27T14:26:24.629306",
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
    "id": 232222017,
    "state": "EXECUTED",
    "date": "2018-07-06T22:32:10.495465",
    "operationAmount": {
        "amount": "37160.27",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 23177857685058835559",
    "to": "Счет 56363465303962313778"
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
    "from": "Visa Classic 4062745111784804",
    "to": "Maestro 8602249654751155"
  }
]

operation_information_1 = """08.12.2019 Открытие вклада
Счет **5907
41096.24 USD
"""

operation_information_2 = """14.10.2018 Перевод со счета на счет
Счет **8655 -> Счет **3493
77751.04 руб.
"""

operation_information_3 = """27.09.2018 Перевод с карты на карту
Maestro 4598 30** **** 4501 -> Visa Platinum 1246 37** **** 3588
50870.71 руб.
"""


@pytest.fixture
def filename_fixture():
    return filename


@pytest.fixture
def data_fixture():
    return data_list.copy()


@pytest.fixture
def last_operations_fixture():
    return last_operations.copy()


@pytest.fixture
def info_fixture_1():
    return operation_information_1


@pytest.fixture
def info_fixture_2():
    return operation_information_2


@pytest.fixture
def info_fixture_3():
    return operation_information_3
