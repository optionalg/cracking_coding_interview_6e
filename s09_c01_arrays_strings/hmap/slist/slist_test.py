from slist import Slist
import pytest


def test_prepend():
    l = Slist()
    l.prepend("Bob")
    assert l.head.key == "Bob"
    assert l.head.next is None


def test_insert():
    l = Slist()
    l.append("Bob")
    l.append("Amy")
    assert l.head.key == "Bob"
    head_next = l.head.next
    assert head_next.key == "Amy"


def test_next():
    l = Slist()
    l.prepend("Bob")
    l.prepend("Amy")
    l.prepend("Carol")
    assert l.head.key == "Carol"
    head_next = l.head.next
    assert head_next.key == "Amy"
    last = head_next.next
    assert last.key == "Bob"


def test_search():
    l = Slist()
    l.prepend("Bob")
    l.prepend("Amy")
    l.prepend("Carol")
    found = l.contains("Bob")
    assert found is True
    found = l.contains("Amy")
    assert found is True
    found = l.contains("Bob")
    assert found is True

    l = Slist()
    l.prepend("Bob")
    l.prepend("Amy")
    found = l.contains("Bob")
    assert found is True
    found = l.contains("Dave")
    assert found is False


def test_delete():
    l = Slist()
    l.prepend("Bob")
    l.prepend("Amy")
    l.prepend("Carol")
    l.delete("Carol")
    assert l.head.key == "Amy"
    l.delete("Bob")
    assert l.head.next is None

    l = Slist()
    l.prepend("Bob")
    l.prepend("Amy")
    l.prepend("Carol")
    with pytest.raises(ValueError):
        l.delete("Edgar")

    l = Slist()
    with pytest.raises(ValueError):
        l.delete("Edgar")


def test_delete_next_reassignment():
    l = Slist()
    l.prepend("Bob")
    l.prepend("Dave")
    l.prepend("Amy")
    l.prepend("Carol")
    l.delete("Amy")
    l.delete("Dave")
    assert l.head.next.key == "Bob"
