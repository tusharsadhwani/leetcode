from typing import Callable


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Find the rightmost digit that's in ascending order
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # If found, swap it with rightmost digit bigger than it
        # This is required to make the next larger number, because
        # putting a larger digit in a more significant position will
        # get us a larger number.
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the array after i+1.
        # Why? because the rest of the array is in descending order.
        # For the next permutation to be smallest, we need the rest of
        # the numbers to be in ascending order.
        # NOTE that i could be -1 in case the entire array was in
        # descending order, in which case this would flip the whole array.
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
