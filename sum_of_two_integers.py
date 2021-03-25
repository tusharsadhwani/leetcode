import math


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return math.floor(math.log2(2 ** a * 2 ** b))


tests = [
    (
        (1, 2,),
        3,
    ),
    (
        (2, 3,),
        5,
    ),
]
