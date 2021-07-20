def make_board(queens: list[int]) -> list[str]:
    """Converts queens index array into board"""
    n = len(queens)
    board_temp = [['.' for _ in range(n)] for _ in range(n)]
    for row_index, col_index in enumerate(queens):
        board_temp[row_index][col_index] = 'Q'

    return ["".join(row) for row in board_temp]


def is_valid(queens: list[int]) -> bool:
    """Checks whether the last queen can be placed in the board"""
    last = len(queens) - 1
    for index in range(last):
        # diagonal check
        if abs(queens[last] - queens[index]) == last - index:
            return False

        # row check
        if queens[index] == queens[last]:
            return False

    return True


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        boards: list[list[int]] = []

        queens: list[int] = []
        # queens is a one-dimension array, like [1, 3, 0, 2] means
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        # index represents row number and value represents column number

        def dfs(count: int = 0) -> None:
            if count == n:  # n queens have been placed correctly
                boards.append(queens.copy())
                return

            for index in range(n):
                queens.append(index)

                if is_valid(queens):
                    dfs(count+1)

                queens.pop()

        dfs()
        return [make_board(board) for board in boards]


tests = [
    (
        (4,),
        [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
    ),
    (
        (1,),
        [["Q"]],
    ),
]
