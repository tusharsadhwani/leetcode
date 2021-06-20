class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        if len(box) == 0:
            return box

        rows = len(box)
        cols = len(box[0])

        ROCK, OBSTACLE, EMPTY = '#', '*', '.'
        for row in box:
            nearest_obstacle = cols
            for index, cell in reversed(list(enumerate(row))):
                if cell == OBSTACLE:
                    nearest_obstacle = index

                elif cell == ROCK:
                    row[index] = EMPTY
                    row[nearest_obstacle-1] = ROCK
                    nearest_obstacle = nearest_obstacle-1

        rotated_box = [
            [box[rows-1-j][i] for j in range(rows)]
            for i in range(cols)
        ]
        return rotated_box


tests = [
    (
        ([["#", ".", "#"]],),
        [["."],
         ["#"],
         ["#"]],
    ),
    (
        (
            [["#", ".", "*", "."],
             ["#", "#", "*", "."]],
        ),
        [["#", "."],
         ["#", "#"],
         ["*", "*"],
         [".", "."]],
    ),
    (
        (
            [["#", "#", "*", ".", "*", "."],
             ["#", "#", "#", "*", ".", "."],
             ["#", "#", "#", ".", "#", "."]],
        ),
        [[".", "#", "#"],
         [".", "#", "#"],
         ["#", "#", "*"],
         ["#", "*", "."],
         ["#", ".", "*"],
         ["#", ".", "."]],
    ),
]
