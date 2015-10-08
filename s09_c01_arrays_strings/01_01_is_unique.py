"""
Chapter 01 Problem 01 - Is Unique

Implement an algorithm to determine if a string has all unique characters.

What if you cannot use additional data structures?
"""


import unittest


def is_unique(str):
    """
    Return whether a string has all unique characters.

    Time Complexity: O(c)
    Space Complexity: O(c)
    where `c` is the number of distinct characters
    """
    seen = set()
    for letter in list(str):
        if letter in seen:
            return False
        else:
            seen.add(letter)
    return True


class TestIsUnique(unittest.TestCase):

    def test_is_unique(self):
        self.assertTrue(is_unique('asdf'))
        self.assertTrue(is_unique('Airplane'))
        self.assertFalse(is_unique('airplane'))

if __name__ == '__main__':
    unittest.main()
