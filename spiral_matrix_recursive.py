def spiral_layer(
        top: int,
        bottom: int,
        left: int,
        right: int,
        matrix: list[list[int]],
) -> list[int]:
    """Traverses one layer of the matrix spiral into a list"""
    ans = []
    for col in range(left, right+1):
        ans.append(matrix[top][col])

    for row in range(top+1, bottom):
        ans.append(matrix[row][right])

    for col in range(right, left-1, -1):
        ans.append(matrix[bottom][col])

    for row in range(bottom-1, top, -1):
        ans.append(matrix[row][left])

    return ans


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 0:
            return []

        ans: list[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top < bottom and left < right:
            ans.extend(spiral_layer(top, bottom, left, right, matrix))
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if top == bottom:
            ans.extend([matrix[top][col] for col in range(left, right+1)])
        elif left == right:
            ans.extend([matrix[row][left] for row in range(top, bottom+1)])

        return ans


tests = [
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    ),
    (
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    ),
    (
        ([],),
        [],
    ),
]
