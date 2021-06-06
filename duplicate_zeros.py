from typing import Callable


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        output = []
        for num in reversed(arr):
            if num == 0:
                output.append(0)
                output.append(0)
            else:
                output.append(num)

        for index in range(len(arr)):
            arr[index] = output[-1-index]


tests = [
    (
        ([1, 0, 2, 3, 0, 4, 5, 0],),
        [1, 0, 0, 2, 3, 0, 0, 4],
    ),
    (
        ([1, 2, 3],),
        [1, 2, 3],
    ),
]


def validator(
        duplicateZeros: Callable[[list[int]], None],
        inputs: tuple[list[int]],
        expected: list[int],
) -> None:
    arr, = inputs
    duplicateZeros(arr)
    assert arr == expected, (arr, expected)
