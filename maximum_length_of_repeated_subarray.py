# # Method 1 - Optimized brute force: TLE
# from collections import defaultdict
#
# class Solution:
#     def findLength(self, nums1: list[int], nums2: list[int]) -> int:
#         if len(nums1) > len(nums2):
#             return self.findLength(nums2, nums1)
#
#         max_length = 0
#
#         # nums2_indices holds the indices of all places where each
#         # character appears in nums2.
#         nums2_indices: defaultdict[int, list[int]] = defaultdict(list)
#         for index, char in enumerate(nums2):
#             nums2_indices[char].append(index)
#
#         for i, num1 in enumerate(nums1):
#             for j in nums2_indices[num1]:
#                 offset = 0
#                 while (
#                     i + offset < len(nums1)
#                     and j + offset < len(nums2)
#                     and nums1[i+offset] == nums2[j+offset]
#                 ):
#                     offset += 1
#
#                 max_length = max(max_length, offset)
#
#         return max_length


# # Method 2 - Recursive, TLE
# class Solution:
#     def findLength(
#             self,
#             nums1: list[int],
#             nums2: list[int],
#             index1: int = 0,
#             index2: int = 0,
#             current_length: int = 0,
#     ) -> int:
#         # current_length is the length of the longest common subarrays
#         # ending at the two current indices.
#         if index1 >= len(nums1) or index2 >= len(nums2):
#             return current_length
#
#         num1, num2 = nums1[index1], nums2[index2]
#
#         if num1 == num2:
#             return self.findLength(nums1, nums2, index1+1, index2+1, current_length+1)
#
#         return max(
#             current_length,
#             self.findLength(nums1, nums2, index1, index2+1, 0),
#             self.findLength(nums1, nums2, index1+1, index2, 0),
#         )


# Method 3 - Bottom-up DP
from collections import defaultdict


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        cache: defaultdict[int, defaultdict[int, int]] = defaultdict(lambda: defaultdict(int))

        for index1, num1 in enumerate(nums1, start=1):
            for index2, num2 in enumerate(nums2, start=1):
                if num1 == num2:
                    cache[index1][index2] = cache[index1-1][index2-1] + 1
                else:
                    cache[index1][index2] = 0

        return max(val for row in cache.values() for val in row.values())


tests = [
    (
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7],),
        3,
    ),
    (
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0],),
        5,
    ),
    (
        ([5, 14, 53, 80, 48], [50, 47, 3, 80, 83],),
        1,
    ),
]
