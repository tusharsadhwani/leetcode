from typing import Callable


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Find the rightmost number that's in ascending order
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # If found, swap it with rightmost number bigger than it
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the rest of the array
        # Note that i could be -1, which would flip the whole array.
        start, end = i + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


tests = [
    (
        ([1, 2, 3],),
        [1, 3, 2],
    ),
    (
        ([3, 2, 1],),
        [1, 2, 3],
    ),
    (
        ([1],),
        [1],
    ),
    (
        ([1, 1],),
        [1, 1],
    ),
    (
        ([1, 2],),
        [2, 1],
    ),
    (
        ([5, 1, 1],),
        [1, 1, 5],
    ),
    (
        ([1, 5, 1],),
        [5, 1, 1],
    ),
]


def validator(
        nextPermutation: Callable[[list[int]], None],
        inputs: tuple[list[int]],
        expected: list[int],
) -> None:
    nums, = inputs
    nextPermutation(nums)
    assert nums == expected, (nums, expected)
