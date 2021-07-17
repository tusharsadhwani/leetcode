from typing import Optional


def binary_search_left(
        nums: list[int],
        target: int,
        start: Optional[int] = None,
        end: Optional[int] = None,
) -> int:
    """Find leftmost value equal to or greater than target"""
    if len(nums) == 0:
        return 0

    if start is None:
        start = 0
    if end is None:
        end = len(nums) - 1

    # Edge condition
    if target > nums[end]:
        return end + 1

    if end <= start:
        return start

    mid = (start + end) // 2

    if nums[mid] < target:
        return binary_search_left(nums, target, mid+1, end)

    return binary_search_left(nums, target, start, mid)


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Uses paitience sort technique.
        Ref: https://www.youtube.com/watch?v=22s1xxRvy28
        """
        decks: list[int] = []
        for num in nums:
            index = binary_search_left(decks, num)
            if index == len(decks):
                decks.append(num)
            else:
                decks[index] = num

        return len(decks)


tests = [
    (
        ([10, 9, 2, 5, 3, 7, 101, 18],),
        4,
    ),
    (
        ([0, 1, 0, 3, 2, 3],),
        4,
    ),
    (
        ([7, 7, 7, 7, 7, 7, 7],),
        1,
    ),
]
