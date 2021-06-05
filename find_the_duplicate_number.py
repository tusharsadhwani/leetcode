class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for num in nums:
            num = abs(num)
            corresponding_index = num - 1
            if nums[corresponding_index] < 0:
                return num
            else:
                nums[corresponding_index] = -nums[corresponding_index]

        return -1


tests = [
    (
        ([1, 3, 4, 2, 2],),
        2,
    ),
    (
        ([3, 1, 3, 4, 2],),
        3,
    ),
    (
        ([1, 1],),
        1,
    ),
    (
        ([1, 1, 2],),
        1,
    ),
]
