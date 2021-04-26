class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        current = 0
        count = 0
        for num in nums:
            if count == 0:
                current = num
                count = 1
                continue

            if num == current:
                count += 1
            else:
                count -= 1

        return current


tests = [
    (
        ([3, 2, 3],),
        3,
    ),
    (
        ([2, 2, 1, 1, 1, 2, 2],),
        2,
    ),
]
