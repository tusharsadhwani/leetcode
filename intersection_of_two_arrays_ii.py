from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num_counter = Counter(nums1)
        intersection: list[int] = []
        for num in nums2:
            if num_counter[num]:
                intersection.append(num)
                num_counter[num] -= 1

        return intersection
