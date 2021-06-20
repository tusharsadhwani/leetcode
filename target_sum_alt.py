from collections import defaultdict


class Solution:
    """Method 3: Top-down DP (no recursion)"""

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        length = len(nums)
        # NOTE: can also use a 2D array of size [2 * sum(nums) + 1][length], but very inconvenient
        cache = defaultdict(lambda: defaultdict(int))

        # If the target is any larger than the sum of all numbers, answer is automatically 0
        max_target = sum(nums)

        # Base case:
        cache[0][0] = 1

        # NOTE: We don't need to set the rest of cache[X][0] to zero because it is 0 by default
        # for amount in range(-max_target, max_target + 1):
        #     cache[amount][0] = 0

        for length in range(1, len(nums) + 1):
            num = nums[length-1]

            # Range of answers lies within [-max_target, max_target]
            for amount in range(-max_target, max_target + 1):
                cache[amount][length] = (
                    cache[amount+num][length-1] + cache[amount-num][length-1]
                )

        return cache[target][length]


tests = [
    (
        ([1, 1, 1, 1, 1], 3,),
        5,
    ),
    (
        ([1], 1,),
        1,
    ),
    (
        (
            [27, 22, 39, 22, 40, 32, 44, 45, 46, 8, 8, 21, 27, 8, 11, 29, 16, 15, 41, 0], 10,),
        0,
    ),
]
