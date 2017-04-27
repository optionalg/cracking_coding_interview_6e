from palindrome_permutation import palindrome_permutation


def test_palindrome_permutation():
    assert palindrome_permutation('racecar') is True
    assert palindrome_permutation('race car') is True
    assert palindrome_permutation('carrace') is True
    assert palindrome_permutation('firetruck') is False
    assert palindrome_permutation('tact coa') is True
    assert palindrome_permutation('toyotas a a toyota') is True
    assert palindrome_permutation('icy cinema amen') is True
