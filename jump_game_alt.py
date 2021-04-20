class Solution:
    def canJump(self, nums: list[int]) -> bool:
        nums.pop()  # don't care about last number at all in this case
        max_reach = 0

        for jump in nums:
            max_reach = max(jump, max_reach-1)
            if max_reach == 0:
                return False

        return True


tests = [
    (
        ([2, 3, 1, 1, 4],),
        True,
    ),
    (
        ([3, 2, 1, 0, 4],),
        False,
    ),
]
