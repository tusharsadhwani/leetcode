class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        current_max = current_min = nums[0]
        largest = nums[0]
        for num in nums[1:]:
            if num > 0:
                current_max, current_min = (
                    max(num, current_max * num), min(num, current_min * num)
                )
            else:
                current_max, current_min = (
                    max(num, current_min * num), min(num, current_max * num)
                )

            largest = max(largest, current_max)

        return largest


tests = [
    (
        ([2, 3, -2, 4],),
        6,
    ),
    (
        ([-2, 0, -1],),
        0,
    ),
    (
        ([-2, 3, -4],),
        24,
    ),
    (
        ([-4, -3, -2],),
        12,
    ),
]
