from typing import Callable, Optional


def quicksort(
    nums: list[int],
    start: Optional[int] = None,
    end: Optional[int] = None,
) -> None:
    """
    In-place quick sort implementation.

    Algorithm:
    - Choose the first number to be pivot
    - Find out the correct place of pivot.
      Pivot must be at the lowest possible position it can get to, i.e.
      if another num == pivot, pivot should be positioned before num.
    - Swap pivot with its correct position
    - right = pivot's index + 1
    - For every number >= pivot on its left:
        - Find a number < pivot with index > right
        - Set right to that number's index
        - swap number on left with number on right
    - Now, run quicksort on the two halves

    For other algorithms: https://wikipedia.org/wiki/Quicksort#Algorithm
    """
    if start is None:
        start = 0
    if end is None:
        end = len(nums) - 1

    if start >= end:
        return

    pivot = start
    pivot_num = nums[pivot]
    smaller = 0
    i = start
    while i <= end:
        num = nums[i]
        if num < pivot_num:
            smaller += 1
        i += 1

    new_pivot = pivot + smaller

    nums[pivot], nums[new_pivot] = nums[new_pivot], nums[pivot]
    pivot = new_pivot
    pivot_num = nums[pivot]

    # Now, pivot is in the correct place.
    # Time to move all larger numbers to the right
    right = pivot + 1
    left = start
    while left < pivot:
        num = nums[left]
        if num < pivot_num:
            left += 1
            continue

        while right < len(nums) - 1 and nums[right] >= pivot_num:
            right += 1

        nums[left], nums[right] = nums[right], nums[left]
        left += 1

    # Finally, run quicksort on the two halves
    quicksort(nums, start, pivot-1)
    quicksort(nums, pivot+1, end)


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        quicksort(nums)


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
