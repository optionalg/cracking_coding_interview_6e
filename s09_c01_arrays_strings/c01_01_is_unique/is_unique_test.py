from is_unique import is_unique


def test_is_unique():
    assert is_unique('asdf') is True
    assert is_unique('Airplane') is True
    assert is_unique('airplane') is False
