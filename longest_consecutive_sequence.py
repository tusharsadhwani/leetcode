class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_streak = 1
                while num + 1 in num_set:
                    num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


tests = [
    (
        ([100, 4, 200, 1, 3, 2],),
        4,
    ),
    (
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],),
        9,
    ),
]
