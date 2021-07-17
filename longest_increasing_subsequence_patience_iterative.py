def binary_search_left(nums: list[int], target: int) -> int:
    """Find leftmost number equal to or greater than target"""
    start, end = 0, len(nums)

    while start < end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start


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

[7, 7,  7]
