def binary_search(
        nums: list[int],
        target: int,
        start: int,
        end: int,
) -> int:
    """Binary search implementation"""
    while start <= end:
        mid = (start + end) // 2
        mid_num = nums[mid]

        if mid_num == target:
            return mid

        if mid_num < target:
            start = mid+1
        else:
            end = mid-1

    return -1


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            start, end = 0, len(row)-1
            index = binary_search(row, target, start, end)
            if index == -1:
                continue

            return True

        return False


tests = [
    (
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ],
            5,
        ),
        True,
    ),
    (
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ],
            20,
        ),
        False,
    ),
]
