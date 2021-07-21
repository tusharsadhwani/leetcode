from typing import Callable


# Method 3 - permutations/bit manipulation
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        n = len(nums)
        for subset_index in range(2**n):
            subset: list[int] = []
            for index, num in enumerate(nums):
                # if index'th bit is 1
                if (subset_index >> index) & 1:
                    subset.append(num)

            result.append(subset)

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
