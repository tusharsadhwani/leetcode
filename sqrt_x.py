class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        ans: float = x
        tolerance = 0.00000001
        while abs(ans - x/ans) > tolerance:
            ans = (ans + x/ans) / 2

        return int(ans)


tests = [
    (
        (4,),
        2,
    ),
    (
        (8,),
        2,
    ),
]
