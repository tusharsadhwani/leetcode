class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # The trick is to replace numbers at the index of the current
        # number with its negative value, so that we know that we have
        # seen that value before when we encounter it again.
        for number in nums:
            index = abs(number) - 1
            already_seen = nums[index] < 0
            if not already_seen:
                nums[index] = -nums[index]  # marking it as seen

        dissappeared_nums = []
        for index, number in enumerate(nums):
            # this will only ever be true
            # if this index value was never found in the list
            if number > 0:
                dissappeared_nums.append(index+1)

        return dissappeared_nums


tests = [
    (
        ([4, 3, 2, 7, 8, 2, 3, 1],),
        [5, 6],
    ),
    (
        ([1, 1],),
        [2],
    ),
]
