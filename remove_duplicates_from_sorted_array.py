class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        offset = 0
        values: set[int] = set()
        for index, num in enumerate(nums):
            nums[index - offset] = num

            if num in values:
                offset += 1
            else:
                values.add(num)

        new_length = len(nums) - offset
        return new_length
