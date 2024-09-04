#!/usr/bin/python3
"""Prime Game interview question"""


def isprime(n):
    """Check if prime number"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def delete_nums(n, nums):
    """Remove numbers"""
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = 0


def isWinner(x, nums):
    """ Return name of player that won
    """
    nums.sort()
    winner = False
    Maria = 0
    Ben = 0
    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        while True:
            change = False
            for i, n in enumerate(nums2):
                if n > 1 and isprime(n):
                    delete_nums(n, nums2)
                    change = True
                    turn += 1
                    break
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
