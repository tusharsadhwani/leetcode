from typing import Optional


def grid_search(
    board: list[list[str]],
    word: str,
    x: int,
    y: int,
    index: int = 1,
    path: Optional[list[tuple[int, int]]] = None,
    path_set: Optional[set[tuple[int, int]]] = None
) -> bool:
    '''Returns if given word exists in the grid'''
    if path is None:
        path = [(x, y)]
    if path_set is None:
        path_set = set(path)

    if index == len(word):
        return True

    char = word[index]

    rows, cols = len(board), len(board[0])
    for i, j in (-1, 0), (0, -1), (0, 1), (1, 0):
        new_x, new_y = x+i, y+j

        if new_x < 0 or new_x >= rows:
            continue
        if new_y < 0 or new_y >= cols:
            continue

        coordindates = (new_x, new_y)
        if coordindates in path_set:
            continue

        cell = board[new_x][new_y]
        if cell == char:
            path.append(coordindates)
            path_set.add(coordindates)

            found = grid_search(
                board, word, new_x, new_y, index+1, path, path_set
            )
            if found:
                return True

            path.pop()
            path_set.remove(coordindates)

    return False


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(word) == 0:
            return True

        first_letter = word[0]
        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if char == first_letter:
                    found = grid_search(board, word, x, y)
                    if found:
                        return True

        return False


tests = [
    (
        ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'),
        True,
    ),
    (
        ([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCF'),
        False,
    ),
]
