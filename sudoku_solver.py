from typing import Callable


def is_valid(
        board: list[list[str]],
        row: int,
        col: int,
        num: str,
) -> bool:
    # Row check
    for i in range(9):
        if board[i][col] == num:
            return False

    # Column check
    for j in range(9):
        if board[row][j] == num:
            return False

    # Square check
    for i in range(3):
        for j in range(3):
            if board[(row//3)*3 + i][(col//3)*3 + j] == num:
                return False

    return True


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> bool:
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != '.':
                    continue

                for num in "123456789":
                    if is_valid(board, i, j, num):
                        board[i][j] = num

                        # If it's the solution return true
                        if self.solveSudoku(board):
                            return True

                        # Otherwise go back
                        else:
                            board[i][j] = '.'

                # If no number is possible in the curent square, return False
                return False

        # Reaching this point means no '.' is left.
        return True


tests = [
    (
        ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
         ),
        [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]],
    ),
]


def validator(
        solveSudoku: Callable[[list[list[str]]], bool],
        inputs: tuple[list[list[str]]],
        expected: list[list[str]],
) -> None:
    board, = inputs
    solveSudoku(board)
    assert board == expected, (board, expected)
