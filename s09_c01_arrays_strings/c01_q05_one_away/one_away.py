"""
Chapter 01 Problem 05 - One Away

Given two strings, write a function to check if they are <= 1 edits away.

There are three types of edits that can be performed:
    - inserting a character
    - removing a character
    - replacing a character

Example:
    pale,  ple  -> True
    pales, pale -> True
    pale,  bale -> True
    pale,  bake -> False
"""

def one_away(str1, str2, edit_seen=False):
    """
    Return whether two strings are one edit (insertion, removal, replacement) away.

    Time Complexity: O(n)
    Space Complexity: O(n)
    where `n` is the length of the shorter string
    """

    # String lengths are more than two letters apart
    if abs(len(str1) - len(str2)) > 1:
        return False
    # One character left in one of the strings
    elif (len(str1) == 0 and len(str2) == 1) or (len(str1) == 1 and len(str2) == 0):
        return not edit_seen
    # One character left in both strings
    elif len(str1) == len(str2) == 1:
        return not edit_seen or str1 == str2
    # First character is the same
    elif str1[0] == str2[0]:
        return one_away(str1[1:], str2[1:], edit_seen=edit_seen)
    # Represents a letter insertion
    elif str1[0] == str2[1]:
        return not edit_seen and one_away(str1[0:], str2[1:], edit_seen=True)
    # Represents a letter removal
    elif str1[1] == str2[0]:
        return not edit_seen and one_away(str1[1:], str2[0:], edit_seen=True)
    # Represents a letter replacement
    else:
        return not edit_seen and one_away(str1[1:], str2[1:], edit_seen=True)
