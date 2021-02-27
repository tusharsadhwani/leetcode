class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        max_loot: list[int] = [0 for _ in nums]
        for index, num in enumerate(nums):
            if index == 0:
                max_loot[index] = num
            elif index == 1:
                max_loot[index] = max(max_loot[index-1], num)
            else:
                max_loot[index] = max(
                    max_loot[index-1],
                    num + max_loot[index-2]
                )

        return max_loot[-1]


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
