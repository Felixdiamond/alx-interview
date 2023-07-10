#!/usr/bin/python3
"""Module for minOperations function"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The number of H characters to reach.

    Returns:
        int: The minimum number of operations required to reach n H characters.
        If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                dp[i] = dp[j] + (i // j)
                break
    return dp[n]
