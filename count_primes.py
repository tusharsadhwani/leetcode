from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return sum(primes)


tests = [
    (
        (10,),
        4,
    ),
    (
        (0,),
        0,
    ),
    (
        (1,),
        0,
    ),
]
