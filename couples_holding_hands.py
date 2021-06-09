class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        swaps = 0
        positions = {num: index for index, num in enumerate(row)}

        for i, num1 in enumerate(row):
            num2 = num1 + 1 if num1 % 2 == 0 else num1 - 1
            j = positions[num2]

            # check if we need to swap
            if j-i > 1:
                row[i+1], row[j] = row[j], row[i+1]
                positions[row[i+1]] = i+1
                positions[row[j]] = j
                swaps += 1

        return swaps


tests = [
    (
        ([0, 2, 1, 3],),
        1,
    ),
    (
        ([3, 2, 0, 1],),
        0,
    ),
]
