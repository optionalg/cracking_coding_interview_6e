"""
Chapter 01 Problem 02 - Check Permutation

Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(s1, s2):
    """
    Return whether s1 and s2 are permutations of each other.

    Time Complexity: O(nlog(n))
    Space Complexity: O(n)
    where n is max(len(s1), len(s2))
    """
    return sorted(s1) == sorted(s2)
