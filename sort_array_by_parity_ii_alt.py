from typing import Callable


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evens, odds = 0, 1
        end = len(nums)
        while evens < end and odds < end:
            if nums[evens] % 2 == 0:
                evens += 2
            elif nums[odds] % 2 != 0:
                odds += 2
            else:
                nums[evens], nums[odds] = nums[odds], nums[evens]
                evens += 2
                odds += 2

        return nums


tests = [
    (
        ([4, 2, 5, 7],),
        [4, 5, 2, 7],
    ),
    (
        ([2, 3],),
        [2, 3],
    ),
    (
        ([2, 3, 1, 1, 4, 0, 0, 4, 3, 3],),
        [2, 3, 4, 1, 4, 3, 0, 1, 0, 3],
    ),
]


def validator(
        sortArrayByParityII: Callable[[list[int]], list[int]],
        inputs: tuple[list[int]],
        expected: list[int],
) -> None:
    nums, = inputs
    output = sortArrayByParityII(nums)

    sorted_output = sorted(output)
    sorted_expected = sorted(expected)
    assert sorted_output == sorted_expected, (sorted_output, sorted_expected)

    for index, value in enumerate(output):
        assert index % 2 == value % 2, (index % 2, value % 2)
