#!/usr/bin/python3
"""Prime Game interview question"""


def delete_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    b = 0
    m = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        delete_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            b += 1
        else:
            m += 1
    if b > m:
        return "Ben"
    if m > b:
        return "Maria"
    return None
