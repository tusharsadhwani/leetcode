
class Solution:
    def trailingZeroes(self, n: int) -> int:
        twos = fives = 0
        for i in range(2, n+1):
            while i % 2 == 0:
                twos += 1
                i //= 2

            while i % 5 == 0:
                fives += 1
                i //= 5

        tens = min(twos, fives)
        return tens


tests = [
    (
        (3,),
        0,
    ),
    (
        (5,),
        1,
    ),
    (
        (0,),
        0,
    ),
]
