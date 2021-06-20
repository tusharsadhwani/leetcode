class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        combinations = [0 for _ in range(amount + 1)]
        combinations[0] = 1  # 1 way to have 0 amount

        for coin in coins:
            for amt in range(coin, amount+1):
                # Notice that in the Top-Down DP solution, combinations[amt][index] will always stay
                # the same as  combinations[amt][index-1], unless combinations[amt-coin][index] has
                # a non-zero value, in which case it is added to the current value.
                # This means that we only really care about the 1 row above us (index-1), and no
                # other previous data. Meaning we can get away with a single row of old data.
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
