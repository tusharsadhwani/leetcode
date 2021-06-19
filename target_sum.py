from collections import defaultdict
from typing import MutableMapping, Optional

# # Method 1: Recursive
# class Solution:
#     def findTargetSumWays(
#         self,
#         nums: list[int],
#         target: int,
#         length: Optional[int] = None
#     ) -> int:
#         if length is None:
#             length = len(nums)
#
#         # Base cases:
#         if length == 0 and target == 0:
#             return 1     # 1 way: empty set
#
#         if length == 0:  # and target != 0
#             return 0
#
#         last_num = nums[length-1]
#         return (
#             self.findTargetSumWays(nums, target + last_num, length-1)
#             + self.findTargetSumWays(nums, target - last_num, length-1)
#         )


# Method 2: Caching
class Solution:
    def findTargetSumWays(
        self,
        nums: list[int],
        target: int,
        length: Optional[int] = None,
        cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None
    ) -> int:
        if length is None:
            length = len(nums)
        if cache is None:
            cache = defaultdict(lambda: defaultdict(int))

        if length in cache[target]:
            return cache[target][length]

        # Base cases:
        if length == 0 and target == 0:
            return 1     # 1 way: empty set

        if length == 0:  # and target != 0
            return 0

        last_num = nums[length-1]
        result = (
            self.findTargetSumWays(nums, target + last_num, length-1, cache)
            + self.findTargetSumWays(nums, target - last_num, length-1, cache)
        )
        cache[target][length] = result
        return result


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
