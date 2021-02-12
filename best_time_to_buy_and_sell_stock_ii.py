from typing import Optional


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bought_price: Optional[int] = None
        total_profit = 0

        for index, price in enumerate(prices):
            if bought_price is None:
                if index + 1 == len(prices):
                    # last value, no need to do anything
                    break

                next_price = prices[index + 1]
                if next_price > price:
                    bought_price = price

                continue

            if index + 1 == len(prices):
                # last value, sell it on a high
                total_profit += price - bought_price
                break

            next_price = prices[index + 1]
            if next_price < price:
                # at a peak, sell
                total_profit += price - bought_price
                bought_price = None

        return total_profit


tests = [
    (
        ([7, 1, 5, 3, 6, 4],),
        7,
    ),
    (
        ([1, 2, 3, 4, 5],),
        4,
    ),
    (
        ([7, 6, 4, 3, 1],),
        0,
    )
]
