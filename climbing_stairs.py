class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        while n > 0:
            a, b = b, a+b
            n -= 1

        return a


tests = [
    (
        (2,),
        2,
    ),
    (
        (3,),
        3,
    ),
]
