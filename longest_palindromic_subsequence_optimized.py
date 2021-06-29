# # Method 3 - Alt solution, modified as a Bottom-up DP
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         cache: list[list[int]] = [[0 for _ in s] for _ in s]
#
#         # Initialization:
#         for index1 in range(len(s)):
#             cache[index1][-1 - index1] = 1
#
#         for index1 in range(len(s)):
#             for index2 in range(len(s)-index1, len(s)):
#                 char1, char2 = s[index1], s[-1 - index2]
#
#                 if char1 == char2:
#                     result = 2 + cache[index1-1][index2-1]
#                 else:
#                     result = max(
#                         cache[index1][index2-1],
#                         cache[index1-1][index2],
#                     )
#
#                 cache[index1][index2] = result
#
#         return cache[-1][-1]


# Method 4 - Bottom-up DP, Space Optimized
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        prev_cache: list[int] = [0 for _ in s]

        for index1 in range(len(s)):
            cache = [0 for _ in s]
            cache[-1 - index1] = 1

            for index2 in range(len(s)-index1, len(s)):
                char1, char2 = s[index1], s[-1 - index2]

                if char1 == char2:
                    result = 2 + prev_cache[index2-1]
                else:
                    result = max(
                        cache[index2-1],
                        prev_cache[index2],
                    )

                cache[index2] = result

            prev_cache = cache

        return cache[-1]


tests = [
    (
        ("bbbab",),
        4,
    ),
    (
        ("cbbd",),
        2,
    ),
    (
        ("a",),
        1,
    ),
]
