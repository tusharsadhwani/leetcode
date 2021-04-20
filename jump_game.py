class Solution:
    def canJump(self, nums: list[int]) -> bool:
        nums.pop()
        max_jump_distances = [0 for _ in nums]

        for index, jump in enumerate(nums):
            max_jump = max(jump, max_jump_distances[index-1]-1)
            if max_jump == 0:
                return False

            max_jump_distances[index] = max_jump

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
