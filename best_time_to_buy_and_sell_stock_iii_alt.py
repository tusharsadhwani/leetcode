import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Idea: Think of buying and selling as state transitions, as one
        # follows another. Overall we are going to transision between
        # states 4 times because we will do 4 transactions in total.
        #
        # Buying a stock can be thought of as losing money, and selling
        # a stock is gaining money. On every day we can also choose to
        # do nothing.
        one_buy = two_buy = sys.maxsize
        one_profit = two_profit = 0
        for price in prices:
            one_buy = min(one_buy, price)
            one_profit = max(one_profit, price - one_buy)
            two_buy = min(two_buy, price - one_profit)
            two_profit = max(two_profit, price - two_buy)

        return two_profit


tests = [
    (
        ([3, 3, 5, 0, 0, 3, 1, 4],),
        6,
    ),
    (
        ([1, 2, 3, 4, 5],),
        4,
    ),
    (
        ([7, 6, 4, 3, 1],),
        0,
    ),
    (
        ([1],),
        0,
    ),
    (
        ([1, 2],),
        1,
    ),
]
