# # Method 1 - Recursive, TLE
# from typing import Optional
#
#
# class Solution:
#     def longestPalindromeSubseq(
#             self,
#             s: str,
#             index1: Optional[int] = None,
#             index2: Optional[int] = None,
#     ) -> int:
#         if index1 is None or index2 is None:
#             index1, index2 = 0, len(s) - 1
#
#         if index1 >= len(s) or index2 < 0 or index1 >= index2:
#             return 0
#
#         char1, char2 = s[index1], s[index2]
#
#         if char1 == char2:
#             return 2 + self.longestPalindromeSubseq(s, index1+1, index2-1)
#
#         return max(
#             self.longestPalindromeSubseq(s, index1, index2-1),
#             self.longestPalindromeSubseq(s, index1+1, index2),
#         )


# Method 2 - Memoization
from collections import defaultdict
from typing import MutableMapping, Optional


class Solution:
    def longestPalindromeSubseq(
            self,
            s: str,
            index1: Optional[int] = None,
            index2: Optional[int] = None,
            cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None,
    ) -> int:
        if index1 is None or index2 is None or cache is None:
            index1, index2 = 0, len(s) - 1
            cache = defaultdict(lambda: defaultdict(int))

        if index1 >= len(s) or index2 < 0 or index1 > index2:
            return 0

        # Edge case:
        if index1 == index2:
            return 1

        if index2 in cache[index1]:
            return cache[index1][index2]

        char1, char2 = s[index1], s[index2]

        if char1 == char2:
            result = 2 + self.longestPalindromeSubseq(s, index1+1, index2-1, cache)
        else:
            result = max(
                self.longestPalindromeSubseq(s, index1, index2-1, cache),
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
