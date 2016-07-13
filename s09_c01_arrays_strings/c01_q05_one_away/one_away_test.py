from one_away import one_away

def test_one_away():
    assert one_away("pale", "ple") is True
    assert one_away("pales", "pale") is True
    assert one_away("pale", "bale") is True
    assert one_away("pale", "bake") is False
    assert one_away("pale", "paleee") is False
    assert one_away("pale", "pe") is False
