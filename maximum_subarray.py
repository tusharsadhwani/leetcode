from typing import Optional


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum: Optional[int] = None
        current_sum: Optional[int] = None

        for num in nums:
            if current_sum is None:
                current_sum = num
            else:
                current_sum += num

            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        assert max_sum is not None
        return max_sum


tests = [
    (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4],),
        6,
    ),
    (
        ([1],),
        1,
    ),
    (
        ([0],),
        0,
    ),
    (
        ([-1],),
        -1,
    ),
    (
        ([-100000],),
        -100000,
    ),
]
