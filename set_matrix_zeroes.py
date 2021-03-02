from typing import Callable


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        first_column_zero = False
        for row in matrix:
            for j, cell in enumerate(row):
                if cell != 0:
                    continue

                row[0] = 0
                if j == 0:
                    first_column_zero = True
                else:
                    matrix[0][j] = 0

        for i, row in enumerate(matrix[1:], start=1):
            for j, cell in enumerate(row[1:], start=1):
                if row[0] == 0:
                    row[j] = 0

                if matrix[0][j] == 0:
                    matrix[i][j] = 0

        # first row check
        if matrix[0][0] == 0:
            first_row = matrix[0]
            for i in range(len(first_row)):
                first_row[i] = 0

        # first column check
        if first_column_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


tests = [
    (
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],),
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
    ),
    (
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],),
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    ),
    (
        ([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]],),
        [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    ),

]


def validator(
        setZeroes: Callable[[list[list[int]]], None],
        inputs: tuple[list[list[int]]],
        expected: list[list[int]]
) -> None:
    matrix, = inputs
    matrix = [row.copy() for row in matrix]
    setZeroes(matrix)
    assert matrix == expected, (matrix, expected)
