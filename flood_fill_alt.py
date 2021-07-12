class Solution:
    def floodFill(self, image: list[list[int]], row: int, col: int, new_color: int) -> list[list[int]]:
        if len(image) == 0:
            return image

        rows, cols = len(image), len(image[0])
        original_color = image[row][col]

        # Edge case: start color is already the same as end color
        #
        # NOTE: because we used visited array in other example, this
        # edge case didn't matter because it didn't cause an infinite loop.
        if original_color == new_color:
            return image

        # NOTE: visited array is not needed as we can use image pixels
        # themselves to figure out if we have visited a cell
        def flood(row: int, col: int) -> None:
            # Base case
            if image[row][col] != original_color:
                return

            image[row][col] = new_color

            #            top           left          right         bottom
            neighbours = (row, col-1), (row-1, col), (row+1, col), (row, col+1)
            for new_row, new_col in neighbours:
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                flood(new_row, new_col)

        flood(row, col)
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
    (
        ([[0, 0, 0], [0, 1, 1]], 1, 1, 1,),
        [[0, 0, 0], [0, 1, 1]],
    ),
]
