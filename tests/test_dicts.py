from utils import dicts


def test_get_val():
    assert dicts.get_val({"mitsubishi": "japan", "audi": "germany",
                          "kia": "south korea", "toyota": "japan"}, "audi") == "germany"
    assert dicts.get_val({"mitsubishi": "japan", "audi": "germany",
                          "kia": "south korea", "toyota": "japan"}, "volvo") == "git"
    assert dicts.get_val(("mitsubishi", "audi", "kia", "toyota"), "audi") == "git"
