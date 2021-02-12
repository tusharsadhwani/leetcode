class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num

        return ans


tests = [
    (
        ([2, 2, 1],),
        1,
    ),
    (
        ([4, 1, 2, 1, 2],),
        4,
    ),
    (
        ([1],),
        1,
    ),
]
