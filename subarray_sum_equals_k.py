from itertools import accumulate
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Sliding window won't work because negative values.
        subarray_count = 0
        subarray_sums = list(accumulate(nums))

        subarray_sums_dict: defaultdict[int, int] = defaultdict(int)
        subarray_sums_dict[0] = 1

        for _sum in subarray_sums:
            subarray_count += subarray_sums_dict[_sum-k]
            subarray_sums_dict[_sum] += 1

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
