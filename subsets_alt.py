from typing import Callable, Optional


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets: list[list[int]] = [[]]

        for num in nums:
            subsets_with_num = [subset + [num] for subset in subsets]
            subsets += subsets_with_num

        return subsets


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
