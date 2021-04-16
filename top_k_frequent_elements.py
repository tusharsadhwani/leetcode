from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        bucket: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for num, frequency in Counter(nums).items():
            bucket[frequency].append(num)

        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]


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
