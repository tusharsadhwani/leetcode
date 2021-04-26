from typing import Callable


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            return self.myPow(x*x, n // 2)

        return x * self.myPow(x*x, n // 2)


tests = [
    (
        (2.00000, 10,),
        1024.00000,
    ),
    (
        (2.10000, 3,),
        9.26100,
    ),
    (
        (2.00000, -2,),
        0.25000,
    ),
]


def validator(
        myPow: Callable[[float, int], int],
        inputs: tuple[float, int],
        expected: float
) -> None:
    x, n = inputs
    raw_output = myPow(x, n)
    output = round(raw_output, 5)
    assert output == expected, (output, expected)
