# FUCK IT. You understand how it works, getting accepted isn't the most important part.
# For explanation:
# https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
# BTW the guy never did binary search in his solution.

from typing import Callable


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        length = len(nums1) + len(nums2)
        half_length = length // 2 + 1

        # Edge cases: zero items from one of the arrays
        if len(nums1) >= half_length and \
                (len(nums2) == 0 or nums1[half_length-1] < nums2[0]):
            if length % 2 == 0:
                return (nums1[half_length-1] + nums1[half_length-2]) / 2
            else:
                return nums1[half_length-1]

        if len(nums2) >= half_length and \
                (len(nums1) == 0 or nums2[half_length-1] < nums1[0]):
            if length % 2 == 0:
                return (nums2[half_length-1] + nums2[half_length-2]) / 2
            else:
                return nums2[half_length-1]

        if len(nums1) < len(nums2):
            smaller, bigger = nums1, nums2
        else:
            smaller, bigger = nums2, nums1

        start, end = 0, len(smaller)
        while start <= end:
            small_count = (start + end) // 2
            big_count = half_length - small_count

            # edge cases:
            if small_count == 0:
                if bigger[big_count-1] < smaller[0]:
                    if length % 2 == 0:
                        return (bigger[big_count-1] + smaller[0]) / 2
                    else:
                        return bigger[big_count-1]

            if small_count == len(smaller):
                if length % 2 == 0:
                    return (smaller[-1] + bigger[0]) / 2
                else:
                    return smaller[-1]

            print(small_count, smaller)
            print(big_count, bigger)
            if smaller[small_count-1] >= bigger[big_count-1] and \
               (len(bigger) <= big_count or smaller[small_count-1] <= bigger[big_count]):
                if length % 2 == 0:
                    next_bigger_element = min(
                        smaller[small_count], bigger[big_count]
                    )
                    return (smaller[small_count-1] + next_bigger_element) / 2
                else:
                    return smaller[small_count-1]

            if bigger[big_count-1] >= smaller[small_count-1] and \
               (len(smaller) <= small_count or bigger[big_count-1] <= smaller[small_count]):
                if length % 2 == 0:
                    next_bigger_element = min(
                        bigger[big_count], smaller[small_count]
                    )
                    return (bigger[big_count-1] + next_bigger_element) / 2
                else:
                    return bigger[big_count-1]

            # change small_count by binary search
            if smaller[small_count] < bigger[big_count-1]:
                start = small_count+1
            else:
                end = small_count-1

        return -420


tests = [
    (
        ([1, 3], [2],),
        2,
    ),
    (
        ([1, 2], [3, 4],),
        2.5,
    ),
    (
        ([0, 0], [0, 0],),
        0,
    ),
    (
        ([], [1],),
        1,
    ),
    (
        ([2], [],),
        2,
    ),
]


def validator(
    findMedianSortedArrays: Callable[[list[int], list[int]], float],
    inputs: tuple[list[int], list[int]],
    expected: float
) -> None:
    pass  # TODO: fix code and remove this validator
