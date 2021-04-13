from typing import Callable


def subets_resursive(
        nums: list[int],
        ans: list[list[int]],
        start: int = 0,
        curr: list[int] = []
) -> None:
    """Recursive implementation of subsets using backtracking"""
    ans.append(curr[:])
    n = len(nums)
    for i in range(start, n):
        curr.append(nums[i])
        subets_resursive(nums, ans, i + 1, curr)
        curr.pop()


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        subets_resursive(nums, ans)
        return ans


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
