class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = temp = 0
        for i in range(31, -1, -1):
            # If (divisor * 2**i) is smaller than dividend,
            # add 2**i to quotient
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i

        ans = sign * quotient
        return min(ans, 2**31 - 1)


tests = [
    (
        (10, 3,),
        3,
    ),
    # (
    #     (7, -3,),
    #     -2,
    # ),
    # (
    #     (0, 1,),
    #     0,
    # ),
    # (
    #     (1, 1,),
    #     1,
    # ),
]
