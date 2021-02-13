from typing import Callable


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = [[0 for _ in row] for row in matrix]
        n = len(matrix)

        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                new_matrix[i][j] = matrix[n-1 - j][i]

        for i, row in enumerate(new_matrix):
            for j, cell in enumerate(row):
                matrix[i][j] = cell


tests = [
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
    ),
    (
        ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ),
    (
        ([[1]],),
        [[1]],
    ),
    (
        ([[1, 2], [3, 4]],),
        [[3, 1], [4, 2]],
    ),
]


def validator(
        rotate: Callable[[list[list[int]]], None],
        inputs: tuple[list[list[int]]],
        expected: list[list[int]]
) -> None:
    matrix, = inputs
    rotate(matrix)
    assert matrix == expected, (matrix, expected)
