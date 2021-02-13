from typing import Callable


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        for index in range(len(s)//2):
            s[index], s[end-index] = s[end-index], s[index]


tests = [
    (
        (["h", "e", "l", "l", "o"],),
        ["o", "l", "l", "e", "h"],
    ),
    (
        (["H", "a", "n", "n", "a", "h"],),
        ["h", "a", "n", "n", "a", "H"],
    ),
]


def validator(
        reverseString: Callable[[list[str]], None],
        inputs: tuple[list[str]],
        expected: list[str]
) -> None:
    nums, = inputs
    reverseString(nums)
    assert nums == expected, (nums, expected)
