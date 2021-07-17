from typing import Callable


# Solution with no extra space
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Approach:
        # - Everything in [0, zeroes_index) is 0's
        # - Everything in [zeroes_index, ones_index) is 1's
        # - Everything in [ones_index, twos_index] we don't know about
        # - Everything in (twos_index, end] is 2's
        # What this means is,
        # We just need to make [ones_index, twos_index] empty,
        # i.e. ones_index > twos_index.
        # To do that:
        # - Start zeroes and ones index on left and twos index on right
        # - Iterate with ones index
        # - For every 0 you see, swap it with zeroes index and increment both indices
        #   * Here, note that zeroes index will never already be pointing to a
        #     pre-existing zero unless both of them point to the same number.
        #     This is because ones index is always >= zeroes index, and we know
        #     that every element before ones index is a zero.
        # - For every 1 you see just increment ones index
        # - For every 2 you see swap it with twos index, and decrement twos index
        #   and don't increment ones index.

        zeroes_index = 0
        ones_index = 0
        twos_index = len(nums) - 1

        while ones_index <= twos_index:
            num = nums[ones_index]
            if num == 0:
                nums[ones_index], nums[zeroes_index] = nums[zeroes_index], nums[ones_index]
                zeroes_index += 1
                ones_index += 1

            elif num == 2:
                nums[ones_index], nums[twos_index] = nums[twos_index], nums[ones_index]
                twos_index -= 1

            else:
                ones_index += 1


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
    (
        ([0, 0, 2, 1, 2, 0, 1],),
        [0, 0, 0, 1, 1, 2, 2],
    )
]


def validator(
    sortColors: Callable[[list[int]], None],
    inputs: tuple[list[int]],
    expected: list[int]
) -> None:
    nums, = inputs
    nums = nums.copy()
    sortColors(nums)
    assert nums == expected, (nums, expected)
