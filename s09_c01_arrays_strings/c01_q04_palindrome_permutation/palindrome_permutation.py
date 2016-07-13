from collections import Counter

"""
Chapter 01 Problem 04 - Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome.

A palindrome is a word/phrase that is the same forwards & backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Example:
    Input:
        Tact Coa
    Output:
        True (permutations: "taco cat", "atco cta", etc.)
"""

def palindrome_permutation(str):
    """
    Return whether the input string is a permutation of a palindrome.

    Approach:
        Even # characters:
            There must be an even number of occurrences of each letter present.
        Odd # characters:
            Same as above, but ONE letter may occur an odd number of times.
            (the middle letter in a palindrome).

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    fixed = str.lower().replace(' ', '')
    counter = Counter(fixed)
    odd_char_seen = False

    if len(fixed) % 2 == 0:
        odd_char_seen = True
    for key, val in dict(counter).iteritems():
        if odd_char_seen and val % 2 != 0:
            return False
        elif not odd_char_seen and val % 2 != 0:
            odd_char_seen = True
        else:
            continue
    return True
