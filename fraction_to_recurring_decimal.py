class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        negative = (numerator < 0) ^ (denominator < 0)
        sign = '-' if negative else ''
        numerator, denominator = abs(numerator), abs(denominator)

        output = ''
        previous_numerators: dict[int, int] = {}

        place_count = len(str(numerator // denominator))
        counter = 1
        while numerator > 0:
            print(f'{place_count=} {output=}')
            if numerator in previous_numerators:
                recurring_start = previous_numerators[numerator]
                non_recurring_part = output[:recurring_start]
                recurring_part = output[recurring_start:]
                output = f'{non_recurring_part}({recurring_part})'
                break

            previous_numerators[numerator] = counter

            if place_count == 0:
                output += '.'

            new_digits = str(numerator // denominator)
            output += new_digits
            numerator %= denominator
            numerator *= 10

            place_count -= len(new_digits)
            counter += len(new_digits)

        return sign + output


tests = [
    (
        (1, 2,),
        '0.5',
    ),
    (
        (2, 1,),
        '2',
    ),
    (
        (2, 3,),
        '0.(6)',
    ),
    (
        (4, 333,),
        '0.(012)',
    ),
    (
        (-1, 5,),
        '-0.2',
    ),
    (
        (22, 7,),
        '3.(142857)',
    ),
    (
        (2147483647, 37,),
        "58040098.(567)",
    )
]
