from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c = round(sqrt(a**2 + b**2))
                # Optimization, break out of b's loop when c gets above n
                if c > n:
                    break

                if a**2 + b**2 == c**2:
                    count += 1

        return count


tests = [
    (
        (5,),
        2,
    ),
    (
        (10,),
        4,
    ),
    (
        (12,),
        4,
    ),
]
