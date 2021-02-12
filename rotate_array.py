class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


tests = [
    (
        ([1, 2, 3, 4, 5, 6, 7], 3),
        [5, 6, 7, 1, 2, 3, 4],
    ),
    (
        ([-1, -100, 3, 99], 2),
        [3, 99, -1, -100],
    )
]


def validator(rotate, inputs, output):
    nums, k = inputs
    rotate(nums, k)
    assert output == nums
