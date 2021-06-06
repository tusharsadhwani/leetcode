from typing import Callable


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = ones = twos = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        index = 0
        for _ in range(zeroes):
            nums[index] = 0
            index += 1
        for _ in range(ones):
            nums[index] = 1
            index += 1
        for _ in range(twos):
            nums[index] = 2
            index += 1


tests = [
    (
        ([2, 0, 2, 1, 1, 0],),
        [0, 0, 1, 1, 2, 2],
    ),
    (
        ([2, 0, 1],),
        [0, 1, 2],
    ),
    (
        ([0],),
        [0],
    ),
    (
        ([1, 1],),
        [1, 1],
    ),
    (
        ([0, 2, 1],),
        [0, 1, 2],
    ),
    (
        ([0, 1, 2],),
        [0, 1, 2],
    ),
    (
        ([1, 2, 0],),
        [0, 1, 2],
    ),
    (
        ([1, 2, 2, 2, 2, 0, 0, 0, 1, 1],),
        [0, 0, 0, 1, 1, 1, 2, 2, 2, 2],
    ),

]


def validator(
    sortColors: Callable[[list[int]], None],
    inputs: tuple[list[int]],
    expected: list[int]
) -> None:
    nums, = inputs
    sortColors(nums)
    assert nums == expected, (nums, expected)
