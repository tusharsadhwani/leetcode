# Method 4 - Bottom-up DP, optimized
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        combinations = [0 for _ in range(amount + 1)]
        combinations[0] = 1  # 1 way to have 0 amount

        for coin in coins:
            for amt in range(coin, amount+1):
                # Notice that in the Bottom-up DP solution, combinations[amt][index] only depends
                # on combinations[amt-coin][index] and combinations[amt][index-1].
                # This means that we only really care about the 1 row above us (index-1), and no
                # other previous data. Meaning we can get away with a single row of cache.
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
    (
        (500, [3, 5, 7, 8, 9, 10, 11],),
        35502874,
    ),
]
