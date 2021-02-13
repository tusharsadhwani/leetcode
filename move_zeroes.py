from typing import Callable


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = index_copy = end = len(nums) - 1

        while index >= 0:
            num = nums[index]
            if num == 0:
                while index < end:
                    nums[index], nums[index+1] = nums[index+1], nums[index]
                    index += 1
                index = index_copy
                end -= 1

            index -= 1
            index_copy = index


tests = [
    (
        ([0, 1, 0, 3, 12],),
        [1, 3, 12, 0, 0],
    ),
]


def validator(
        moveZeroes: Callable[[list[int]], None],
        inputs: tuple[list[int]],
        expected: list[int]
) -> None:
    nums, = inputs
    moveZeroes(nums)
    assert nums == expected, (nums, expected)
