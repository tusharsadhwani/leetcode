from itertools import accumulate


class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        total = sum(arr)
        if total % 3 != 0:
            return False

        one_third = total // 3

        partial_sums = list(accumulate(arr))

        if one_third not in partial_sums:
            return False

        one_third_index = partial_sums.index(one_third)

        # i+1:-1 because we don't want the 2nd or last array to be empty
        if 2*one_third not in partial_sums[one_third_index+1:-1]:
            return False

        return True


tests = [
    (
        ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1],),
        True,
    ),
    (
        ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1],),
        False,
    ),
    (
        ([3, 3, 6, 5, -2, 2, 5, 1, -9, 4],),
        True,
    ),
    (
        ([6, 1, 1, 13, -1, 0, -10, 20],),
        False,
    ),
    (
        ([0, 0, 0, 0],),
        True,
    ),
    (
        ([29, 31, 27, -10, -67, 22, 15, -1, -16, -29, 59, -18, 48],),
        True,
    ),
    (
        ([1, -1, 1, -1],),
        False,
    ),
]
