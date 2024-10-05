#!/usr/bin/python3
"""Module for prime game."""


def isWinner(x, nums):
    """Returns name of player that won most rounds."""
    if x <= 0 or not nums:
        return None

    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    prime_kaunts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_kaunts[i] = prime_kaunts[i - 1] + (1 if sieve[i] else 0)

    maria_win = 0
    ben_win = 0

    for n in nums:
        if prime_kaunts[n] % 2 == 0:
            ben_win += 1
        else:
            maria_win += 1

    if maria_win > ben_win:
        return "Maria"
    elif ben_win > maria_win:
        return "Ben"
    else:
        return None
