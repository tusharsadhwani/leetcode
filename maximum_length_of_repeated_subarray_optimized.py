# Method 4 - Bottom-up DP, Space Optimized
from collections import defaultdict


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        cache: defaultdict[int, int] = defaultdict(int)

        max_length = 0

        for num1 in nums1:
            prev_cache = cache.copy()  # since we depend on values behind us, which we are changing.
            for index, num2 in enumerate(nums2, start=1):
                if num1 != num2:
                    # NOTE: NOW we have to make sure to set it to zero.
                    cache[index] = 0
                    continue

                current_length = prev_cache[index-1] + 1
                cache[index] = current_length

                # Keeping track of all-time maximum, so no need to worry about lost data.
                max_length = max(max_length, current_length)

        return max_length


tests = [
    (
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7],),
        3,
    ),
    (
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0],),
        5,
    ),
    (
        ([5, 14, 53, 80, 48], [50, 47, 3, 80, 83],),
        1,
    ),
    (
        ([1, 0, 0, 0, 1], [1, 0, 0, 1, 1],),
        3,
    ),
]
