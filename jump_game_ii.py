import sys
from collections import defaultdict
from typing import MutableMapping, Optional

# # Method 1 - Recursion: TLE
#
# class Solution:
#     def jump(self, nums: list[int], index: int = 0) -> int:
#         end = len(nums) - 1
#
#         if index >= end:
#             return 0
#
#         num = nums[index]
#         min_jumps = sys.maxsize
#         for jump_offset in range(1, num+1):
#             min_jumps = min(min_jumps, self.jump(nums, index+jump_offset))
#
#         return 1 + min_jumps


# Method 2 - Memoization
class Solution:
    def jump(
            self,
            nums: list[int],
            index: int = 0,
            cache: Optional[MutableMapping[int, int]] = None,
    ) -> int:
        if cache is None:
            cache = defaultdict(int)

        end = len(nums) - 1

        if index >= end:
            return 0

        if index in cache:
            return cache[index]

        num = nums[index]
        min_jumps = sys.maxsize
        for jump_offset in range(1, num+1):
            min_jumps = min(min_jumps, self.jump(nums, index+jump_offset, cache))

        cache[index] = 1 + min_jumps
        return 1 + min_jumps


tests = [
    (
        ([2, 3, 1, 1, 4],),
        2,
    ),
    (
        ([2, 3, 0, 1, 4],),
        2,
    ),
]
