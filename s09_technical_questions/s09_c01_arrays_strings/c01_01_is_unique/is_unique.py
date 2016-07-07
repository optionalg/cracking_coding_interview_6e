"""
Chapter 01 Problem 01 - Is Unique

Implement an algorithm to determine if a string has all unique characters.

What if you cannot use additional data structures?
"""

def is_unique(str):
    """
    Return whether a string has all unique characters.
    Assume upper/lowercase variants are different letters.

    Time Complexity: O(c)
    Space Complexity: O(c)
    where `c` is the number of distinct characters

    If alphabet is ASCII, c = 128.
    If alphabet is extended ASCII, c = 256.
    """
    return len(set(str)) == len(str)

def is_unique_no_additional_data_structures(str):
    """
    Return whether a string has all unique characters.
    Assume upper/lowercase variants are different letters.

    Time Complexity: O(c^2)
    Space Complexity: O(1)
    where `c` is the number of distinct characters

    If alphabet is ASCII, c = 128.
    If alphabet is extended ASCII, c = 256.
    """
    for i1 in range(len(str)):
        for i2 in range(len(str)):
            if i1 != i2 and str[i1] == str[i2]:
                return False
    return True
