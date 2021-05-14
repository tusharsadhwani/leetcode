class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i, n in enumerate(arr):
            for j, m in enumerate(arr):
                if i == j:
                    continue

                if m == 2 * n:
                    return True

        return False


tests = [
    (
        ([10, 2, 5, 3],),
        True,
    ),
    (
        ([7, 1, 14, 11],),
        True,
    ),
    (
        ([3, 1, 7, 11],),
        False,
    ),
]
