from typing import Optional


def binary_search(
        array: list[int],
        value: int,
        start: Optional[int] = None,
        end: Optional[int] = None,
) -> int:
    """Returns if given number exists in an array"""
    if start is None or end is None:
        start, end = 0, len(array)-1

    if start < 0 or start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == value:
        return mid

    if array[mid] < value:
        return binary_search(array, value, mid+1, end)

    return binary_search(array, value, start, mid-1)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, num in enumerate(nums):
            complement = target - num
            for complement_index, _ in enumerate(nums[index+1:], index+1):
                if nums[complement_index] == complement:
                    return [index, complement_index]

        return [-1, -1]


tests = [
    (
        ([2, 7, 11, 15], 9,),
        [0, 1],
    ),
    (
        ([3, 2, 4], 6),
        [1, 2],
    ),
    (
        ([3, 3], 6,),
        [0, 1],
    ),

]
