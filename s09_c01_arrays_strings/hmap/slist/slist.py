"""
Singly-linked list implementation in Python.
"""


class Node(object):
    """
    An instance represents a node in a singly-linked list.
    """

    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class Slist(object):
    """
    An instance represents a singly-linked list.
    """

    def __init__(self):
        self.head = None

    def append(self, key, val=None):
        """
        Append a node containing key to the end of the list.
        """
        cur = self.head
        while cur and cur.next:
            cur = cur.next
        if cur:
            cur.next = Node(key, val, None)
        else:
            self.head = Node(key, val, None)

    def prepend(self, key, val=None):
        """
        Prepend a node containing key at the start of the list.
        """
        new = Node(key, val, self.head)
        self.head = new

    def size(self):
        """
        Return the size of this list.
        """
        cur = self.head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def contains(self, key):
        """
        Return whether this list contains a node with specific key.
        """
        cur = self.head
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False

    def get(self, key):
        """
        Return whether this list contains a node with specific key.
        """
        cur = self.head
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        raise ValueError("key not in list")

    def delete(self, key):
        """
        Delete the node in this list with specific key, if applicable.
        """
        prev = None
        cur = self.head
        found = False

        while cur and not found:
            if cur.key == key:
                found = True
            else:
                prev = cur
                cur = cur.next

        if cur is None:
            raise ValueError("key not in list")
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
