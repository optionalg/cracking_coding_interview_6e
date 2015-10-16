"""
HashMap implementation in Python.
"""


from slist import slist

class Hmap:
    """
    An instance represents a HashMap.
    """

    def __init__(self, size=5):
        self.size = size
        self.buckets = [None] * size


    def hash(self, key):
        """
        Hash a key. Simply mod the key with the size of the HashMap.
        """
        return int(key) % self.size


    def add(self, key, val):
        """
        Add a (key, value) pair to the HashMap.
        """
        hash = self.hash(key)
        if self.buckets[hash] is None:
            self.buckets[hash] = slist.Slist()
        self.buckets[hash].prepend(key, val)


    def get(self, key):
        """
        Get the value corresponding to key 'key' from the HashMap.
        """
        hash = self.hash(key)
        return self.buckets[hash].get(key)


    def contains(self, key):
        """
        Return whether key 'key' is in the HashMap.
        """
        hash = self.hash(key)
        return self.buckets[hash].contains(key)
