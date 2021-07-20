from itertools import accumulate
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # NOTE: Sliding window won't work because negative values.

        # Approach:
        # Every subarray sum can be expressed as:
        # partial_sum[i] - partial_sum[j]
        # where partial_sum[x] is sum from 0 to x, and i > j.
        # So for every partial_sum, we can check if (partial_sum - k)
        # has occured before, and for each occurence we have an
        # equivalent subarray that is a valid solution.
        subarray_count = 0
        partial_sums = accumulate(nums, initial=0)
        partial_sum_count: defaultdict[int, int] = defaultdict(int)

        for partial_sum in partial_sums:
            rest = partial_sum - k
            subarray_count += partial_sum_count[rest]

            partial_sum_count[partial_sum] += 1

        return subarray_count


tests = [
    (
        ([1, 1, 1], 2,),
        2,
    ),
    (
        ([1, 2, 3], 3,),
        2,
    ),
    (
        ([1], 1,),
        1,
    ),

    (
        ([-1, -1, 1], 0,),
        1,
    ),
]
