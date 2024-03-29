class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Approach: keep track of the highest price in the future,
        # and iterate backwards to find the largest difference.
        max_price = prices[-1]
        max_profit = 0
        for price in reversed(prices):
            if price > max_price:
                max_price = price

            profit = max_price - price
            if profit > max_profit:
                max_profit = profit

        return max_profit


tests = [
    (
        ([7, 1, 5, 3, 6, 4],),
        5,
    ),
    (
        ([7, 6, 4, 3, 1],),
        0,
    )
]
