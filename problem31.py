"""
Coin Sums
Project Euler Problem #31
by Muaz Siddiqui

In England the currency is made up of pound, £, and pence, p, and there are eight
coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

import time
def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]

# Recursive implementation pop a coin and get to value + reduce value and use all coins
@memoize
def count_change(value, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
    if value == 0:
        return 1
    elif value < 0 or len(coins) == 0:
        return 0
    return count_change(value, coins[1:]) + count_change(value - coins[0], coins)

def answer():
    start = time.time()
    x = count_change(200)
    elapsed = time.time() - start
    print(str(x) + " ways to count 2 Pounds, solved in " + str(elapsed) +" seconds")
