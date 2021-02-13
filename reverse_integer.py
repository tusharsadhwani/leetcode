class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(abs(x))
        reversed_str = x_str[::-1]

        int_max = (1 << 31) - 1

        reversed_num = 0
        for digit_str in reversed_str:
            digit = int(digit_str)
            if (reversed_num > int_max // 10 or
                    reversed_num == int_max // 10 and digit > 7):
                return 0

            reversed_num *= 10
            reversed_num += digit

        if x < 0:
            reversed_num *= -1
        return reversed_num


tests = [
    (
        (123,),
        321,
    ),
    (
        (-123,),
        -321,
    ),
    (
        (120,),
        21,
    ),
    (
        (0,),
        0,
    ),
]
