from typing import Callable


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        pos1 = m - 1
        pos2 = n - 1
        endpos = len(nums1) - 1

        while pos1 >= 0 and pos2 >= 0:
            val1 = nums1[pos1]
            val2 = nums2[pos2]

            if val1 > val2:
                nums1[endpos] = val1
                pos1 -= 1
            else:
                nums1[endpos] = val2
                pos2 -= 1

            endpos -= 1

        while pos1 >= 0:
            nums1[endpos] = nums1[pos1]
            pos1 -= 1
            endpos -= 1

        while pos2 >= 0:
            nums1[endpos] = nums2[pos2]
            pos2 -= 1
            endpos -= 1


tests = [
    (
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3,),
        [1, 2, 2, 3, 5, 6],
    ),
    (
        ([1], 1, [], 0,),
        [1],
    ),
    (
        ([0], 0, [1], 1,),
        [1],
    ),
]


def validator(
        merge: Callable[[list[int], int, list[int], int], None],
        inputs: tuple[list[int], int, list[int], int],
        expected: list[int],
) -> None:
    nums1, m, nums2, n = inputs
    merge(nums1, m, nums2, n)
    assert nums1 == expected, (nums1, expected)
