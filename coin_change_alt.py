from collections import defaultdict
import sys

# # Method 1 - Recursive: Stack Overflow
# def coin_change(coins: list[int], amount: int, index: int = 0) -> int:
#     if index >= len(coins):
#         return sys.maxsize
#
#     coin = coins[index]
#
#     # Base cases:
#     if amount < 0:
#         return sys.maxsize
#
#     if amount == 0:
#         return 0
#
#     rest_amount = amount - coin
#
#     # Case 1: take this coin, and add 1 to previous min coin count
#     case_1 = 1 + coin_change(coins, rest_amount, index)
#     # Case 2: don't take this coin anymore
#     case_2 = coin_change(coins, amount, index+1)
#
#     return min(case_1, case_2)


# # Method 2 - Memoization: Stack Overflow
# from typing import MutableMapping, Optional
#
# def coin_change(
#         coins: list[int],
#         amount: int,
#         index: int = 0,
#         cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None,
# ) -> int:
#     if cache is None:
#         cache: defaultdict[int, defaultdict[int, int]] = defaultdict(lambda: defaultdict(int))
#
#     if index >= len(coins):
#         return sys.maxsize
#
#     if index in cache[amount]:
#         return cache[amount][index]
#
#     # Base cases:
#     if amount < 0:
#         return sys.maxsize
#
#     if amount == 0:
#         return 0
#
#     coin = coins[index]
#     rest_amount = amount - coin
#
#     # Case 1: take this coin, and add 1 to previous min coin count
#     case_1 = 1 + coin_change(coins, rest_amount, index, cache)
#     # Case 2: don't take this coin anymore
#     case_2 = coin_change(coins, amount, index+1, cache)
#
#     min_coin_count = min(case_1, case_2)
#     cache[amount][index] = min_coin_count
#     return min_coin_count


# Method 3 - Bottom-up DP
def coin_change(coins: list[int], amount: int) -> int:
    cache: defaultdict[int, defaultdict[int, int]] = defaultdict(lambda: defaultdict(int))
    length = len(coins)

    # NOTE: No need to set zeroes, it is zero by default
    # for index in range(length+1):
    #     cache[0][index] = 0

    for amt in range(1, amount+1):
        cache[amt][0] = sys.maxsize

    # Index 0 is reserved for no coins.
    for index, coin in enumerate(coins, start=1):
        for amt in range(1, amount + 1):
            rest_amount = amt - coin

            # Case 1: take this coin, and add 1 to previous min coin count
            if rest_amount < 0:
                case_1 = sys.maxsize
            else:
                case_1 = 1 + cache[rest_amount][index]

            # Case 2: don't take this coin anymore
            case_2 = cache[amt][index-1]

            min_coin_count = min(case_1, case_2)
            cache[amt][index] = min_coin_count

    return cache[amount][length]


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
