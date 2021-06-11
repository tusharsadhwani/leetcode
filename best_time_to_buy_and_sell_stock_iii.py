######################################
#########  O(n^2) algorithm  #########
######################################
# def get_single_max_profit(prices: list[int]) -> int:
#     lowest = sys.maxsize
#     max_profit = 0
#     for price in prices:
#         if price < lowest:
#             lowest = price
#
#         profit = price - lowest
#         max_profit = max(max_profit, profit)
#
#     return max_profit
#
#
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         profit = 0
#         for index in range(len(prices)):
#             left, right = prices[:index], prices[index:]
#             left_profit = get_single_max_profit(left)
#             right_profit = get_single_max_profit(right)
#             profit = max(profit, left_profit + right_profit)
#
#         return profit


# An optimized version of that same idea:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = 0

        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max


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
