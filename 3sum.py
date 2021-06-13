class Solution:
    def threeSum(self, nums: list[int]) -> list[tuple[int, int, int]]:
        nums.sort()

        result: list[tuple[int, int, int]] = []
        for index, num in enumerate(nums):
            # Checking if num is duplicate
            if index > 0 and num == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1

                elif three_sum < 0:
                    left += 1

                else:
                    result.append((num, nums[left], nums[right]))
                    # Prevent duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


tests = [
    (
        ([-1, 0, 1, 2, -1, -4],),
        [(-1, -1, 2), (-1, 0, 1)],
    ),
    (
        ([],),
        [],
    ),
    (
        ([0],),
        [],
    ),
]
