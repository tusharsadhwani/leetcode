class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [0 for _ in nums]
        ans = 0
        for i in range(len(nums)):
            max_length = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length = max(max_length, dp[j])

            dp[i] = 1 + max_length
            ans = max(ans, dp[i])

        return ans


tests = [
    (
        ([10, 9, 2, 5, 3, 7, 101, 18],),
        4,
    ),
    (
        ([0, 1, 0, 3, 2, 3],),
        4,
    ),
    (
        ([7, 7, 7, 7, 7, 7, 7],),
        1,
    ),
]
