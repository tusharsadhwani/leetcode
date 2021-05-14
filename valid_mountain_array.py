class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        descending = False

        if len(arr) <= 1:
            return False

        if arr[0] >= arr[1]:
            return False

        prev_num = arr[0]
        for num in arr[1:]:
            if num == prev_num:
                return False

            if not descending and num < prev_num:
                descending = True

            elif descending and num > prev_num:
                return False

            prev_num = num

        return descending


tests = [
    (
        ([2, 1],),
        False,
    ),
    (
        ([3, 5, 5],),
        False,
    ),
    (
        ([0, 3, 2, 1],),
        True,
    ),
]
