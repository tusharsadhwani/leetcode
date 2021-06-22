from collections import defaultdict


class Solution:
    """Method 4: Bottom-up DP, optimized"""

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        length = len(nums)
        cache: defaultdict[int, int] = defaultdict(int)

        max_target = sum(nums)

        cache[0] = 1
        for length in range(1, len(nums) + 1):
            num = nums[length-1]

            prev_cache = cache.copy()  # since we depend on values behind us, which we are changing.
            for amount in range(-max_target, max_target + 1):
                # Since we only depend on values in (length-1), we can
                # get away with a single row of cache.
                cache[amount] = (
                    prev_cache[amount+num] + prev_cache[amount-num]
                )

        return cache[target]


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
