class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        return n & (n-1) == 0


tests = [
    (
        (1,),
        True,
    ),
    (
        (16,),
        True,
    ),
    (
        (3,),
        False,
    ),
    (
        (4,),
        True,
    ),
    (
        (5,),
        False,
    ),
]
