from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap: list[int] = []
        for i in range(k):
            heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])

        return min_heap[0]


tests = [
    (
        ([3, 2, 1, 5, 6, 4], 2,),
        5,
    ),
    (
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4,),
        4,
    ),
]
