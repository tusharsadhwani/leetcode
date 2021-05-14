class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        for index, num in enumerate(nums):
            if num % 2 == 1:
                leftmost_odd = index
                break
        else:  # All evens
            return nums

        for index, num in reversed(list(enumerate(nums))):
            if num % 2 == 0:
                rightmost_even = index
                break
        else:  # All odds
            return nums

        while leftmost_odd < rightmost_even:
            nums[leftmost_odd], nums[rightmost_even] = nums[rightmost_even], nums[leftmost_odd]

            while leftmost_odd < len(nums) and nums[leftmost_odd] % 2 == 0:
                leftmost_odd += 1

            while rightmost_even >= 0 and nums[rightmost_even] % 2 == 1:
                rightmost_even -= 1

        return nums


tests = [
    (
        ([3, 1, 2, 4],),
        [2, 4, 3, 1],
    ),
]


def validator(method, inputs, expected):
    pass  # TODO
