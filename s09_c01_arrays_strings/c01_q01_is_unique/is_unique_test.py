from is_unique import is_unique, is_unique_no_additional_data_structures


def test_is_unique():
    assert is_unique("test") is False
    assert is_unique("Test") is True
    assert is_unique("qwertyuiopasdfghjklzxcvbnm") is True
    assert is_unique("qwertyuiopasdfghjklzxcvbnmq") is False


def test_is_unique_no_additional_data_structures():
    assert is_unique_no_additional_data_structures("test") is False
    assert is_unique_no_additional_data_structures("Test") is True
    assert is_unique_no_additional_data_structures("qwertyuiopasdfghjklzxcvbnm") is True
    assert is_unique_no_additional_data_structures("qwertyuiopasdfghjklzxcvbnmq") is False
