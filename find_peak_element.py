class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if mid == start:  # edge case, where end - start == 1
                return start if nums[start] > nums[end] else end

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] < nums[mid+1]:
                start = mid+1
            else:
                end = mid-1

        return start


tests = [
    (
        ([1, 2, 3, 1],),
        2,
    ),
    (
        ([1, 2, 1, 3, 5, 6, 4],),
        5,
    ),
]
