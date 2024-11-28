#!/usr/bin/python3
"""making change challenge
"""


def makeChange(coins, total):
    """Returns the number of coins needed to meet the total
    """
    if total <= 0:
        return 0
    if (coins is None or len(coins) == 0):
        return -1
    change = 0
    avaib_coins = sorted(coins, reverse=True)
    change_left = total
    for coin in avaib_coins:
        while (change_left % coin >= 0 and change_left >= coin):
            change += int(change_left / coin)
            change_left = change_left % coin
    if change_left != 0:
        change = -1
    return change
