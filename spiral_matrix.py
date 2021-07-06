class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 0:
            return []

        ans: list[int] = []
        rows, cols = len(matrix), len(matrix[0])
        up, down, left, right = 0, rows - 1, 0, cols - 1
        while left < right and up < down:
            ans.extend(matrix[up][i] for i in range(left, right))
            ans.extend(matrix[i][right] for i in range(up, down))
            ans.extend(matrix[down][i] for i in range(right, left, -1))
            ans.extend(matrix[i][left] for i in range(down, up, -1))

            up, down, left, right = up+1, down-1, left+1, right-1

        if left == right:
            ans.extend(matrix[i][right] for i in range(up, down+1))

        # elif is important, to not double count the 1 center element
        elif up == down:
            ans.extend(matrix[up][j] for j in range(left, right+1))

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
