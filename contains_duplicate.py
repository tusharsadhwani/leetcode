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
