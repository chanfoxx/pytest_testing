import pytest


@pytest.fixture
def coll_fixture():
    return {"mitsubishi": "japan", "audi": "germany",
                          "kia": "south korea", "toyota": "japan"}
