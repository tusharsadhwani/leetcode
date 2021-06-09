from collections import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        counter = Counter(nums)
        operations = 0
        for num, count in counter.items():
            other = k - num
            if other in counter:
                other_count = counter[other]
                operations += min(count, other_count)

        # Since we will be double counting everything,
        return operations // 2


tests = [
    (
        ([1, 2, 3, 4], 5,),
        2,
    ),
    (
        ([3, 1, 3, 4, 3], 6,),
        1,
    ),
]
