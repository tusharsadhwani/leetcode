def has_repeat_digits(grid: list[list[str]]) -> bool:
    """Returns if given 2d grid has repeating digit strings"""
    digit_strings = {str(i) for i in range(1, 10)}
    for row in grid:
        for digit in row:
            if digit == '.':
                continue

            if digit not in digit_strings:
                return True

            digit_strings.remove(digit)

    return False


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            grid = [row]
            if has_repeat_digits(grid):
                return False

        rows = len(board)
        columns = [[row[i] for row in board] for i in range(rows)]
        for column in columns:
            grid = [column]
            if has_repeat_digits(grid):
                return False

        for i in range(3):
            for j in range(3):
                grid = [[board[row][col]
                         for col in range(3*j, 3*(j+1))]
                        for row in range(3*i, 3*(i+1))]

                if has_repeat_digits(grid):
                    return False

        return True


tests = [
    (
        ([
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],),
        True,
    ),
    (
        ([
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],),
        False,
    ),
]
