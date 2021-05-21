import sys


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        minus_inf = -sys.maxsize
        first = second = third = minus_inf

        for num in nums:
            if num > first:
                first, second, third = num, first, second

            elif first > num > second:
                second, third = num, second

            elif second > num > third:
                third = num

        return first if third is minus_inf else third


tests = [
    (
        ([3, 2, 1],),
        1,
    ),
    (
        ([1, 2],),
        2,
    ),
    (
        ([2, 2, 3, 1],),
        1,
    ),
]
