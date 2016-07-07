from hmap import Hmap
import pytest


def test():
    map = Hmap()
    map.add(1, 2)
    assert map.contains(1) is True
    assert map.get(1) == 2

    map.add(10, "hello")
    assert map.contains(10) is True
    assert map.get(10) == "hello"

    map.add(14, "hello")
    assert map.contains(14) is True
    assert map.get(14) == "hello"

    map.add(15, "hello")
    assert map.contains(15) is True
    assert map.get(15) == "hello"
