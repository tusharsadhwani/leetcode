class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        reversed_digits = digits[::-1]

        carry = True
        for index, digit in enumerate(reversed_digits):
            if carry:
                digit += 1
                if digit == 10:
                    digit = 0
                else:
                    carry = False
            else:
                break
            reversed_digits[index] = digit

        if carry:
            reversed_digits.append(1)

        return reversed_digits[::-1]


tests = [
    (
        ([1, 2, 3],),
        [1, 2, 4],
    ),
    (
        ([4, 3, 2, 1],),
        [4, 3, 2, 2],
    ),
    (
        ([0],),
        [1],
    ),
]
