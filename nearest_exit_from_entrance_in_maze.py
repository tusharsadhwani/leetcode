import sys
from collections import deque


def setup_edge_cell(
        maze: list[list[str]],
        exit_distances: list[list[int]],
        queue: deque[tuple[int, int]],
        visited: list[list[bool]],
        entrance: tuple[int, int],
        i: int,
        j: int,
) -> None:
    row, col = entrance
    if row == i and col == j:
        return

    if visited[i][j]:
        return

    cell = maze[i][j]
    if cell == '+':
        return

    exit_distances[i][j] = 0
    visited[i][j] = True
    queue.append((i, j))


def visit_neighbours(
        maze: list[list[str]],
        exit_distances: list[list[int]],
        queue: deque[tuple[int, int]],
        visited: list[list[bool]],
        i: int,
        j: int,
) -> None:
    if maze[i][j] == '+':
        return

    rows, cols = len(exit_distances), len(exit_distances[0])
    neighbours = (i, j-1), (i-1, j), (i+1, j), (i, j+1)

    for new_i, new_j in neighbours:
        if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
            continue

        if visited[new_i][new_j]:
            continue

        current_distance = exit_distances[new_i][new_j]
        exit_distances[new_i][new_j] = min(current_distance, 1 + exit_distances[i][j])
        visited[new_i][new_j] = True
        queue.append((new_i, new_j))


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: tuple[int, int]) -> int:
        exit_distances = [[sys.maxsize for _ in row] for row in maze]
        visited = [[False for _ in row] for row in maze]

        if len(maze) == 0:
            return -1

        rows, cols = len(maze), len(maze[0])

        queue: deque[tuple[int, int]] = deque()
        # top row
        for col in range(cols):
            setup_edge_cell(maze, exit_distances, queue, visited, entrance, 0, col)
        # bottom row
        for col in range(cols):
            setup_edge_cell(maze, exit_distances, queue, visited, entrance, rows-1, col)
        # left column
        for row in range(rows):
            setup_edge_cell(maze, exit_distances, queue, visited, entrance, row, 0)
        # right column
        for row in range(rows):
            setup_edge_cell(maze, exit_distances, queue, visited, entrance, row, cols-1)

        while queue:
            row, col = queue.popleft()
            visit_neighbours(maze, exit_distances, queue, visited, row, col)

        row, col = entrance
        distance = exit_distances[row][col]
        return -1 if distance >= sys.maxsize else distance


tests = [
    (
        ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], (1, 2),),
        1,
    ),
    (
        ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], (1, 0),),
        2,
    ),
    (
        ([[".", "+"]], (0, 0),),
        -1,
    ),
]
