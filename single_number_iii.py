from typing import Callable


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num

        # At this point, xor == num1 ^ num2.

        # The x & (x-1) trick removes the last `1` in a number.
        # so, XORing it with x keeps only the rightmost `1` bit.
        # Realistically we just needed any 1 bit that's different in the
        # two numbers, but this works too.
        different_bit = (xor & (xor-1)) ^ xor

        # Now we want to differentiate between num1 and num2, and to be
        # able to do that, we can just divide the array into two parts:
        # those who have that one bit set, and those who don't.
        # We can use any one of those halves to solve for 1 number, like
        # we did in the first single_number.
        filtered_nums = [n for n in nums if n & different_bit != 0]
        num1 = 0
        for num in filtered_nums:
            num1 ^= num

        num2 = xor ^ num1
        return [num1, num2]


tests = [
    (
        ([1, 2, 1, 3, 2, 5],),
        [3, 5],
    ),
    (
        ([-1, 0],),
        [-1, 0],
    ),
    (
        ([0, 1],),
        [1, 0],
    ),
]


def validator(
        singleNumber: Callable[[list[int]], tuple[int, int]],
        inputs: tuple[list[int]],
        expected: tuple[int, int],
) -> None:
    nums, = inputs
    output = singleNumber(nums)

    output_set = set(output)
    expected_set = set(expected)
    assert output_set == expected_set, (output_set, expected_set)
