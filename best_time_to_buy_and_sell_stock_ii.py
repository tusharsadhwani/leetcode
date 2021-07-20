from typing import Optional


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Appproach: buy at every valley, sell at every peak
        # (i.e. when a[i] > a[i-1] and a[i] > a[i+1]).
        # To do that, we will buy on every moment we are guaranteed a
        # profit, i.e. whenever the immediately next value is bigger.
        # Then we sell whenever the immediately next value is smaller.
        # The only exception is selling at the last value if we have
        # already bought something (since technically that is the peak
        # and you can say the next value is 0)
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
