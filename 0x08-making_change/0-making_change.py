#!/usr/bin/python3
"""Module to solve coin change probelm w/ dynamic programming."""


def makeChange(coins, total):
    """Calculates fewest coins needed to make total."""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
