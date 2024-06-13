#!/usr/bin/python3
"""
Minimum Operations
interview qst
"""


def minOperations(n):
    """
    Function: minOperations
    Return: int
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
