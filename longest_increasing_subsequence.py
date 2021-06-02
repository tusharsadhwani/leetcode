class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        longest_per_index = [0 for _ in nums]
        longest_so_far = 0
        for i in range(len(nums)):
            max_length = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length = max(max_length, longest_per_index[j])

            longest_per_index[i] = 1 + max_length
            longest_so_far = max(longest_so_far, longest_per_index[i])

        return longest_so_far


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
