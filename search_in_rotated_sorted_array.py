def binary_search(
        nums: list[int],
        target: int,
        start: int,
        end: int,
        shift: int
) -> int:
    """Binary search implementation"""
    size = len(nums)
    while start <= end:
        mid = (start + end) // 2
        rotated_index = get_rotated_index(shift, size, mid)
        mid_num = nums[rotated_index]

        if mid_num == target:
            return rotated_index

        if mid_num < target:
            start = mid+1
        else:
            end = mid-1

    return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start_index = get_start_index(nums)
        start, end = 0, len(nums)-1
        return binary_search(nums, target, start, end, start_index)


def get_start_index(nums: list[int]) -> int:
    """Get the actual first index of rotated array"""
    prev = nums[0]
    for index, num in enumerate(nums):
        if num < prev:
            return index

        prev = num

    return 0


def get_rotated_index(start: int, size: int, index: int) -> int:
    """Get the rotated index of the array"""
    return (index + start) % size


tests = [
    (
        ([4, 5, 6, 7, 0, 1, 2], 0,),
        4,
    ),
    (
        ([4, 5, 6, 7, 0, 1, 2], 3,),
        -1,
    ),
    (
        ([1], 0,),
        -1,
    ),
]
