class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        largest_value = -1
        for index, num in reversed(list(enumerate(arr))):
            arr[index] = largest_value
            largest_value = max(largest_value, num)

        return arr


tests = [
    (
        ([17, 18, 5, 4, 6, 1],),
        [18, 6, 6, 6, 1, -1],
    ),
    (
        ([400],),
        [-1],
    ),
]
