import sys


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        smallest, second_smallest = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True

        return False


tests = [
    (
        ([1, 2, 3, 4, 5],),
        True,
    ),
    (
        ([5, 4, 3, 2, 1],),
        False,
    ),
    (
        ([2, 1, 5, 0, 4, 6],),
        True,
    ),
]
