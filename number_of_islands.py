
def flood(
        grid: list[list[str]],
        value: str,
        row: int,
        col: int,
        visited: list[list[bool]]) -> None:
    """Recursively floods grid to mark visited cells as True"""
    visited[row][col] = True

    rows, cols = len(grid), len(grid[0])

    for i, j in (-1, 0), (0, -1), (0, 1), (1, 0):
        new_row, new_col = row+i, col+j
        if new_row < 0 or new_row >= rows:
            continue
        if new_col < 0 or new_col >= cols:
            continue

        if visited[new_row][new_col]:
            continue

        if grid[new_row][new_col] == value:
            flood(grid, value, new_row, new_col, visited)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0

        value = '1'
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == value and not visited[i][j]:
                    count += 1
                    flood(grid, value, i, j, visited)

        return count


tests = [
    (
        ([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],),
        1,
    ),
    (
        ([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],),
        3,
    ),
]
