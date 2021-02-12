class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        index = 1
        end = len(nums)
        while index < end:
            if nums[index] == nums[index - 1]:
                return True

            index += 1

        return False


tests = [
    (
        ([1, 2, 3, 1],),
        True,
    ),
    (
        ([1, 2, 3, 4],),
        False,
    ),
    (
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),
        True,
    ),
]
