"""
Singly-linked list implementation in Python.
"""


class Node(object):
    """
    An instance represents a node in a singly-linked list.
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Slist(object):
    """
    An instance represents a singly-linked list.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a node containing data to the end of the list.
        """
        cur = self.head
        while cur and cur.next:
            cur = cur.next
        if cur:
            cur.next = Node(data, None)
        else:
            self.head = Node(data, None)

    def prepend(self, data):
        """
        Prepend a node containing data at the start of the list.
        """
        new = Node(data, self.head)
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

    def contains(self, data):
        """
        Return whether this list contains a node with specific data.
        """
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def get(self, data):
        """
        Return whether this list contains a node with specific data.
        """
        cur = self.head
        while cur:
            if cur.data == data:
                return data
            cur = cur.next
        raise ValueError("Data not in list")

    def delete(self, data):
        """
        Delete the node in this list with specific data, if applicable.
        """
        prev = None
        cur = self.head
        found = False

        while cur and not found:
            if cur.data == data:
                found = True
            else:
                prev = cur
                cur = cur.next

        if cur is None:
            raise ValueError("Data not in list")
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
