class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        size = len(nums)
        nearest_multiple_of_4 = size if size % 4 == 0 else size - size % 4 + 4

        zero_present = False
        xor = 0
        for num in nums:
            if num == 0:
                zero_present = True

            xor ^= num

        for num in range(size+1, nearest_multiple_of_4):
            xor ^= num

        if xor != 0:
            return xor

        if not zero_present:
            return 0

        return size


tests = [
    (
        ([3, 0, 1],),
        2,
    ),
    (
        ([0, 1],),
        2,
    ),
    (
        ([9, 6, 4, 2, 3, 5, 7, 0, 1],),
        8,
    ),
    (
        ([0],),
        1,
    ),
    (
        ([1, 3, 2],),
        0,
    ),
]
