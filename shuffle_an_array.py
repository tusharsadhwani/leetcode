import random
from typing import Callable


class Solution:
    # def __init__(self, nums: list[int]):
    #     self.nums = nums

    # def reset(self) -> list[int]:
    #     """Resets the array to its original configuration and return it."""
    #     return self.nums

    def shuffle(self, nums: list[int]) -> list[int]:
        """Returns a random shuffling of the array."""
        nums = nums.copy()
        length = len(nums)
        for index in range(length):
            random_index = random.randrange(length)
            nums[index], nums[random_index] = nums[random_index], nums[index]

        return nums


tests = [
    (
        ([1, 2, 3],),
        None,
    ),
]


def validator(
        shuffle: Callable[[list[int]], list[int]],
        inputs: tuple[list[int]],
        _: None,
) -> None:
    nums, = inputs
    shuffled = shuffle(nums)
    assert len(nums) == len(shuffled), (len(nums), len(shuffled))
    nums_set, shuffled_set = set(nums), set(shuffled)
    assert nums_set == shuffled_set
