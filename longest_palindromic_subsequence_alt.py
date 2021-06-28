from typing import MutableMapping, Optional
from collections import defaultdict


# # Method 1 - Recursive, with (0,0) as starting point
# class Solution:
#     def longestPalindromeSubseq(
#             self,
#             s: str,
#             index1: int = 0,
#             index2: int = 0,
#     ) -> int:
#         if index1 >= len(s) or index2 >= len(s) or index1 + index2 >= len(s):
#             return 0
#
#         # Edge case:
#         if index1 + index2 == len(s) - 1:
#             return 1
#
#         char1, char2 = s[index1], s[-1 - index2]
#
#         if char1 == char2:
#             return 2 + self.longestPalindromeSubseq(s, index1+1, index2+1)
#
#         return max(
#             self.longestPalindromeSubseq(s, index1, index2+1),
#             self.longestPalindromeSubseq(s, index1+1, index2),
#         )


# Method 2 - Memoization, with (0, 0) as start
class Solution:
    def longestPalindromeSubseq(
            self,
            s: str,
            index1: int = 0,
            index2: int = 0,
            cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None,
    ) -> int:
        if cache is None:
            cache = defaultdict(lambda: defaultdict(int))

        if index1 >= len(s) or index2 >= len(s) or index1 + index2 >= len(s):
            return 0

        # Edge case:
        if index1 + index2 == len(s) - 1:
            return 1

        if index2 in cache[index1]:
            return cache[index1][index2]

        char1, char2 = s[index1], s[-1 - index2]

        if char1 == char2:
            result = 2 + self.longestPalindromeSubseq(s, index1+1, index2+1, cache)
        else:
            result = max(
                self.longestPalindromeSubseq(s, index1, index2+1, cache),
                self.longestPalindromeSubseq(s, index1+1, index2, cache),
            )

        cache[index1][index2] = result
        return result


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
