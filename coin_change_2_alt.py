from collections import defaultdict


# Method 3: Top-Down DP
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        cache = defaultdict(lambda: defaultdict(int))

        # For 0 amount, there's only one way
        for index in range(len(coins) + 1):
            cache[0][index] = 1

        for index, coin in enumerate(coins, start=1):  # index 0 is for empty coin array
            for amt in range(1, amount + 1):
                combinations = 0

                # Case 1: We don't increment current coin count
                combinations += cache[amt][index-1]

                # Case 2: We do increment current coin count
                remaining_amount = amt - coin
                if remaining_amount >= 0:
                    combinations += cache[remaining_amount][index]

                cache[amt][index] = combinations

        return cache[amount][index]


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
