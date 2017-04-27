from urlify import URLify


def test_URLify():
    assert URLify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert URLify("      ", 2) == "%20%20"
