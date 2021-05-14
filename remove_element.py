from typing import Callable


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        offset = 0
        for index, num in enumerate(nums):
            new_index = max(0, index - offset)
            nums[new_index] = num

            if num == val:
                offset += 1

        return len(nums) - offset


tests = [
    (
        ([3, 2, 2, 3], 3,),
        [2, 2],
    ),
    (
        ([0, 1, 2, 2, 3, 0, 4, 2], 2,),
        [0, 1, 4, 0, 3],
    ),
]


def validator(
        removeElement: Callable[[list[int], int], int],
        inputs: tuple[list[int], int],
        expected: list[int],
) -> None:
    nums, val = inputs
    nums = nums.copy()

    length = removeElement(nums, val)
    assert length == len(expected), (length, len(expected))

    output_set = set(nums[:length])
    expected_set = set(expected)
    assert output_set == expected_set, (output_set, expected_set)
