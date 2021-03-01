class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        rows = [[1]]
        for level in range(1, numRows):
            prev_row = rows[level-1]
            new_row = [1]
            for index in range(1, level):
                prev, current = prev_row[index-1], prev_row[index]
                new_row.append(prev + current)

            new_row.append(1)
            rows.append(new_row)

        return rows

        return rows


tests = [
    (
        (5,),
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
    ),
    (
        (1,),
        [[1]],
    ),
]
