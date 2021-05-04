class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        max_count = max(max_count, count)
        return max_count


tests = [
    (
        ([1, 1, 0, 1, 1, 1],),
        3,
    ),
    (
        ([1, 0, 1, 1, 0, 1],),
        2,
    ),
]
