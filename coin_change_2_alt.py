from collections import defaultdict
from typing import MutableMapping, Optional

## Recursion: TLE
# import sys
#
# class Solution:
#     def change(self, amount: int, coins: list[int], index: int = 0) -> int:
#         if amount < 0:
#             return 0
#
#         if amount == 0:
#             return 1
#
#         if index >= len(coins):
#             return 0
#
#         coin = coins[index]
#
#         combinations = 0
#         # Case 1: We don't increment current coin count
#         combinations += self.change(amount, coins, index+1)
#
#         # Case 2: We do increment current coin count
#         remaining_amount = amount - coin
#         combinations += self.change(remaining_amount, coins, index)
#
#         return combinations


# Method 2: Memoization
class Solution:
    def change(
            self,
            amount: int,
            coins: list[int],
            index: int = 0,
            cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None,
    ) -> int:
        if cache is None:
            cache = defaultdict(lambda: defaultdict(int))

        if amount < 0:
            return 0

        if amount == 0:
            return 1

        if index >= len(coins):
            return 0

        if index in cache[amount]:
            return cache[amount][index]

        coin = coins[index]
        combinations = 0

        # Case 1: We don't increment current coin count
        combinations += self.change(amount, coins, index+1, cache)

        # Case 2: We do increment current coin count
        remaining_amount = amount - coin
        combinations += self.change(remaining_amount, coins, index, cache)

        cache[amount][index] = combinations
        return combinations


tests = [
    (
        (5, [1, 2, 5],),
        4,
    ),
    (
        (3, [2],),
        0,
    ),
    (
        (10, [10],),
        1,
    ),
    (
        (500, [3, 5, 7, 8, 9, 10, 11],),
        35502874,
    ),
]
