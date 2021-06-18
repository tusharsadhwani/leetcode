def is_valid(nums: list[int], m: int, mid: int) -> bool:
    # assume mid is < max(nums)
    cuts = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum > mid:
            cuts += 1
            current_sum = num

    parts = cuts + 1
    return parts <= m


class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        # our answer will lie between max(nums) and sum(nums)
        low, high = max(nums), sum(nums)
        answer = low
        while low <= high:
            mid = (low+high) // 2
            # can you make at-most m sub-arrays with maximum sum at-most mid
            if is_valid(nums, m, mid):
                answer, high = mid, mid-1
            else:
                low = mid + 1

        return answer


tests = [
    (
        ([1, 2, 3, 4, 5], 2,),
        9,
    ),
    (
        ([1, 4, 4], 3,),
        4,
    ),
]
