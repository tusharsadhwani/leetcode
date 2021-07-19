from typing import Callable, Optional


# # Method 1 - which honestly I don't understand very well
# class Solution:
#     def subsets(
#             self,
#             nums: list[int],
#             start: int = 0,
#             prefix: Optional[list[int]] = None,
#             result: Optional[list[list[int]]] = None,
#     ) -> list[list[int]]:
#         """Recursive implementation of subsets using backtracking"""
#         if result is None or prefix is None:
#             prefix, result = [], []
#
#         subset = prefix.copy()
#         result.append(subset)
#
#         end = len(nums)
#         for index in range(start, end):
#             prefix.append(nums[index])
#             self.subsets(nums, index+1, prefix, result)
#             prefix.pop()
#
#         return result


# Method 2 - which I understand more easily
class Solution:
    def subsets(
            self,
            nums: list[int],
            index: int = 0,
            prefix: Optional[list[int]] = None,
            result: Optional[list[list[int]]] = None,
    ) -> list[list[int]]:
        """Recursive implementation of subsets using backtracking"""
        if result is None or prefix is None:
            prefix, result = [], []

        end = len(nums)
        if index == end:
            # Base case
            subset = prefix.copy()
            result.append(subset)
            return result

        # for each index, either include the current number
        prefix.append(nums[index])
        self.subsets(nums, index+1, prefix, result)
        # or don't
        prefix.pop()
        self.subsets(nums, index+1, prefix, result)

        return result


tests = [
    (
        ([1, 2, 3],),
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    ),
    (
        ([0],),
        [[], [0]],
    ),
]


def validator(
    subsets: Callable[[list[int]], list[list[int]]],
    inputs: tuple[list[int]],
    expected: list[list[int]],
) -> None:
    nums, = inputs
    output = subsets(nums)
    output.sort()
    expected.sort()
    assert output == expected, (output, expected)
