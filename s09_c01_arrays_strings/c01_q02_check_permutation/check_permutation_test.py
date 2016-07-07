from check_permutation import check_permutation

def test_check_permutation():
    assert check_permutation("hello", "hello") is True
    assert check_permutation("hello", "olleh") is True
    assert check_permutation("hello", "holel") is True
    assert check_permutation("hello", "lehol") is True
    assert check_permutation("helo", "hello") is False
