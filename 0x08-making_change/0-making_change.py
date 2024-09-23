#!/usr/bin/python3
"""Module to solve coin change probelm w/ dynamic programming."""


def makeChange(coins, total):
    """
    Calculates fewest coins needed to make total
    using greedy algo.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_kaunt = 0
    remnant = total

    for coin in coins:
        if remnant >= coin:
            kaunt = remnant // coin
            coin_kaunt += kaunt
            remnant -= kaunt * coin

        if remnant == 0:
            return coin_kaunt

    return -1 if remnant > 0 else coin_kaunt

    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
    """
