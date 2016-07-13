"""
Chapter 01 Problem 03 - URLify

Write a method to replace all spaces in a string with '%20'. Use a character array.

You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.

Example:
    Input:
        "Mr John Smith    ", 13
    Output:
        "Mr%20John%20Smith"
"""

def URLify(str, length):
    """
    Return the input string with all spaces replaced with '%20'.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    char_list = list(str)
    total_len = len(char_list)
    num_spaces = 0
    for char in char_list[0:length]:
        if char == ' ':
            num_spaces += 1

    i = 0
    while (num_spaces > 0):
        if char_list[i] == ' ':
            char_list[i+3:total_len] = char_list[i+1:total_len-2]
            char_list[i:i+3] = ['%', '2', '0']
            num_spaces -= 1
        i += 1
    return ''.join(char_list)
