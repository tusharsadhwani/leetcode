class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


tests = [
    (
        ([12, 345, 2, 6, 7896],),
        2,
    ),
    (
        ([555, 901, 482, 1771],),
        1,
    ),
]
