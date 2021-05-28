class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        nums.sort()

        smallest, largest = nums[0], nums[-1]
        ans = largest - smallest
        for i in range(len(nums)-1):
            # Assuming that i is the middle point, below which everything
            # is considered "small" and after which everything is considered "big".
            # This is even further optimized because of how the intervals behave.
            # Detailed explanation is present here:
            # https://leetcode.com/problems/smallest-range-ii/solution/
            current, next = nums[i], nums[i+1]
            ans = min(ans, max(current+k, largest-k) - min(next-k, smallest+k))

        return ans


tests = [
    (
        ([1], 0,),
        0,
    ),
    (
        ([0, 10], 2,),
        6,
    ),
    (
        ([1, 3, 6], 3,),
        3,
    ),
]
