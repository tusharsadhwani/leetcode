def permute_recursive(nums: list[int]) -> list[list[int]]:
    """Recursive implementation to return all permutations of nums"""
    if len(nums) == 1:
        return [nums]

    ans: list[list[int]] = []
    for index, num in enumerate(nums):
        rest = [num for idx, num in enumerate(nums) if idx != index]
        for perms in permute_recursive(rest):
            ans.append([num, *perms])

    return ans


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permute_recursive(nums)


tests = [
    (
        ([1, 2, 3],),
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
    ),
    (
        ([0, 1],),
        [[0, 1], [1, 0]],
    ),
    (
        ([1],),
        [[1]],
    ),
]
