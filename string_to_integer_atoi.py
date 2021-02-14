class Solution:
    def myAtoi(self, s: str) -> int:
        int_max = (1 << 31) - 1
        int_min = -1 << 31

        number_started = False
        is_negative = False
        num = 0
        for char in s:
            if char == ' ' and not number_started:
                continue

            if char == '+' and not number_started:
                number_started = True
                continue
            elif char == '-' and not number_started:
                is_negative = True
                number_started = True
                continue
            elif not char.isdigit():
                if is_negative:
                    num *= -1
                return num

            number_started = True
            digit = int(char)

            if num > int_max // 10:
                return int_min if is_negative else int_max

            if num == int_max // 10:
                if is_negative and digit > 8:
                    return int_min
                elif not is_negative and digit > 7:
                    return int_max

            num *= 10
            num += digit

        if is_negative:
            num *= -1
        return num


tests = [
    (
        ("42",),
        42,
    ),
    (
        ("   -42",),
        -42,
    ),
    (
        ("4193 with words",),
        4193,
    ),
    (
        ("words and 987",),
        0,
    ),
    (
        ("-91283472332",),
        -2147483648,
    ),
]
