import pytest

from utils import dicts


@pytest.mark.parametrize('collection, key, expected', [
    (("mitsubishi", "audi", "kia", "toyota"), "audi", "unknown value"),
    ({}, "audi", "unknown value"),
    (None, "audi", "unknown value"),
    (123, "audi", "unknown value")
])

def test_get_val(collection, key, expected):
    assert dicts.get_val(collection, key) == expected

def test_get_val__fixture(coll_fixture):
    assert dicts.get_val(coll_fixture, "audi") == "germany"
    assert dicts.get_val(coll_fixture, "volvo") == "unknown value"

def test_get_val__missing_key(coll_fixture):
    with pytest.raises(TypeError):
        dicts.get_val(coll_fixture)
