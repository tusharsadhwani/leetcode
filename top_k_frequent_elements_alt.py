from collections import Counter
import random
from typing import Callable, Counter


def partition(
    count: Counter[int],
    unique: list[int],
    left: int,
    right: int,
    pivot: int,
) -> int:
    """Simple Lomuto's partition, but count based"""
    pivot_count = count[unique[pivot]]
    unique[pivot], unique[right] = unique[right], unique[pivot]

    new_pivot = left
    for i in range(left, right):
        if count[unique[i]] < pivot_count:
            unique[new_pivot], unique[i] = unique[i], unique[new_pivot]
            new_pivot += 1

    unique[right], unique[new_pivot] = unique[new_pivot], unique[right]

    return new_pivot


def quickselect(
    count: Counter[int],
    unique: list[int],
    left: int,
    right: int,
    k: int,
) -> None:
    """
    Sort a list within left..right till kth less frequent element
    takes its place. 
    """
    if left == right:
        return

    pivot_index = random.randint(left, right)
    pivot_index = partition(count, unique, left, right, pivot_index)

    if k == pivot_index:
        return
    elif k < pivot_index:
        quickselect(count, unique, left, pivot_index - 1, k)
    else:
        quickselect(count, unique, pivot_index + 1, right, k)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        unique = list(count.keys())
        n = len(unique)

        quickselect(count, unique, 0, n - 1, n - k)
        return unique[n - k:]


tests = [
    (
        ([1, 1, 1, 2, 2, 3], 2,),
        [1, 2],
    ),
    (
        ([1], 1,),
        [1],
    ),
]


def validator(
    topKFrequent: Callable[[list[int], int], list[int]],
    inputs: tuple[list[int], int],
    expected: list[int]
) -> None:
    nums, k = inputs
    output = topKFrequent(nums, k)
    output_set = set(output)
    expected_set = set(expected)
    assert output_set == expected_set, (output_set, expected_set)
