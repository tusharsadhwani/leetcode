from collections import defaultdict
import sys


# Method 4 - Bottom-up DP, optimized
def coin_change(coins: list[int], amount: int) -> int:
    cache: defaultdict[int, int] = defaultdict(int)

    for amt in range(1, amount+1):
        cache[amt] = sys.maxsize

    for coin in coins:
        for amt in range(1, amount + 1):
            rest_amount = amt - coin

            # Since we only use index and index-1 in the DP,
            # we can get away with a single row of cache.
            if rest_amount < 0:
                case_1 = sys.maxsize
            else:
                case_1 = 1 + cache[rest_amount]

            case_2 = cache[amt]
            min_coin_count = min(case_1, case_2)
            cache[amt] = min_coin_count

    return cache[amount]


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        result = coin_change(coins, amount)
        return -1 if result >= sys.maxsize else result


tests = [
    (
        ([1, 2, 5], 11,),
        3,
    ),
    (
        ([2], 3,),
        -1,
    ),
    (
        ([1], 1,),
        1,
    ),
    (
        ([1], 2,),
        2,
    ),
    (
        ([186, 419, 83, 408], 6249,),
        20,
    ),
    (
        ([3, 7, 405, 436], 8839,),
        25,
    ),
]
