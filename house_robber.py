class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        dp: list[int] = [0 for _ in nums]
        for index, num in enumerate(nums):
            if index == 0:
                dp[index] = num
            elif index == 1:
                dp[index] = max(dp[index-1], num)
            else:
                dp[index] = max(dp[index-1], num + dp[index-2])

        return dp[-1]


tests = [
    (
        ([1, 2, 3, 1],),
        4,
    ),
    (
        ([2, 7, 9, 3, 1],),
        12,
    ),
]
