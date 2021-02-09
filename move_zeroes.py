class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = index_copy = end = len(nums) - 1

        while index >= 0:
            num = nums[index]
            if num == 0:
                while index < end:
                    nums[index], nums[index+1] = nums[index+1], nums[index]
                    index += 1
                index = index_copy
                end -= 1

            index -= 1
            index_copy = index
