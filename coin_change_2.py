import sys

## Recursion: TLE
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


class Solution:
    def change(self, amount: int, coins: list[int], index: int = 0) -> int:
        combinations = [0 for _ in range(amount + 1)]
        combinations[0] = 1

        for coin in coins:
            for amt in range(coin, amount + 1):
                if amt >= coin:
                    combinations[amt] += combinations[amt - coin]

        return combinations[amount]


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
]
