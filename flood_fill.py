from typing import Optional


class Solution:
    def floodFill(
            self,
            image: list[list[int]],
            row: int,
            col: int,
            new_color: int,
            visited: Optional[list[list[bool]]] = None,
            original_color: Optional[int] = None,
    ) -> list[list[int]]:
        if len(image) == 0:
            return image

        # default values
        if visited is None:
            visited = [[False for _ in row] for row in image]
        if original_color is None:
            original_color = image[row][col]

        image[row][col] = new_color

        rows, cols = len(image), len(image[0])

        #            top           left          right         bottom
        neighbours = (row, col-1), (row-1, col), (row+1, col), (row, col+1)
        for new_row, new_col in neighbours:
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue

            if visited[new_row][new_col]:
                continue

            visited[new_row][new_col] = True

            neighbour_color = image[new_row][new_col]
            if neighbour_color == original_color:
                self.floodFill(image, new_row, new_col, new_color, visited, original_color)

        return image


tests = [
    (
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,),
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    ),
    (
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 2,),
        [[2, 2, 2], [2, 2, 2]],
    ),
    (
        ([[0, 0, 0], [0, 1, 0]], 1, 1, 2,),
        [[0, 0, 0], [0, 2, 0]],
    ),
]
