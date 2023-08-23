#!/usr/bin/python3
"""makeChange module"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of the values of the coins in your possession
    :type coins: List[int]
    :param total: Total amount to meet
    :type total: int
    :return: Fewest number of coins needed to meet total. If total is 0 or less,
             return 0. If total cannot be met by any number of coins you have,
             return -1.
    :rtype: int
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total = total % coin
        if total == 0:
            return count
    return -1

