class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)):
                num1, num2 = str(nums[i]), str(nums[j])
                if num1 + num2 > num2 + num1:
                    nums[i], nums[j] = nums[j], nums[i]

        result = ''.join(str(num) for num in nums)
        return str(int(result))  # because of stupid leetcode test case [0, 0]


tests = [
    (
        ([10, 2],),
        "210",
    ),
    (
        ([3, 30, 34, 5, 9],),
        "9534330",
    ),
    (
        ([1],),
        "1",
    ),
    (
        ([10],),
        "10",
    ),
]
