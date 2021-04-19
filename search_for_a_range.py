
def binary_search_start(
        nums: list[int],
        target: int,
        start: int,
        end: int) -> int:
    """Find first index of target"""
    while start <= end:
        if start == end:
            return start if nums[start] == target else -1

        mid = (start + end) // 2
        mid_num = nums[mid]

        if mid_num == target:
            if mid == 0 or nums[mid-1] < target:
                return mid

        if mid_num < target:
            start = mid+1
        else:
            end = mid

    return -1


def binary_search_end(
        nums: list[int],
        target: int,
        start: int,
        end: int) -> int:
    """Find last index of target"""
    while start <= end:
        if start == end:
            return start if nums[start] == target else -1

        mid = (start + end) // 2
        mid_num = nums[mid]

        if mid_num == target:
            if mid == len(nums)-1 or nums[mid+1] > target:
                return mid

        if mid_num > target:
            end = mid
        else:
            start = mid+1

    return -1


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]

        start, end = 0, len(nums) - 1
        pos1 = binary_search_start(nums, target, start, end)
        pos2 = binary_search_end(nums, target, start, end)
        return [pos1, pos2]


tests = [
    (
        ([5, 7, 7, 8, 8, 10], 8,),
        [3, 4],
    ),
    (
        ([5, 7, 7, 8, 8, 10], 6,),
        [-1, -1],
    ),
    (
        ([], 0,),
        [-1, -1],
    ),


]
