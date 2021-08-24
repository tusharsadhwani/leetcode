def get_perimeter(grid: list[list[int]], row: int, col: int) -> int:
    """Returns the perimeter around the given cell in grid"""
    rows, cols = len(grid), len(grid[0])

    perimeter = 4
    neighbours = (row-1, col), (row, col-1), (row, col+1), (row+1, col)
    for i, j in neighbours:
        if i < 0 or i >= rows or j < 0 or j >= cols:
            continue

        # Every 1 that's around the cell is the lack of a border.
        # So subtract 1 from the perimeter.
        if grid[i][j] == 1:
            perimeter -= 1

    return perimeter


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    perimeter += get_perimeter(grid, i, j)

        return perimeter


tests = [
    (
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],),
        16,
    ),
    (
        ([[1]],),
        4,
    ),
    (
        ([[1, 0]],),
        4,
    ),
]
