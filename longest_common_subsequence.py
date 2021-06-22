from collections import defaultdict
from typing import MutableMapping, Optional


# # Method 1 - Recursion: TLE
# class Solution:
#     def longestCommonSubsequence(
#             self,
#             text1: str,
#             text2: str,
#             index1: int = 0,
#             index2: int = 0
#     ) -> int:
#         # Base case: empty string
#         if index1 >= len(text1) or index2 >= len(text2):
#             return 0
#
#         char1, char2 = text1[index1], text2[index2]
#
#         if char1 == char2:
#             return 1 + self.longestCommonSubsequence(text1, text2, index1+1, index2+1)
#
#         return max(
#             self.longestCommonSubsequence(text1, text2, index1, index2+1),
#             self.longestCommonSubsequence(text1, text2, index1+1, index2),
#         )


# Method 2 - Memoization, Top-down DP
class Solution:
    def longestCommonSubsequence(
            self,
            text1: str,
            text2: str,
            index1: int = 0,
            index2: int = 0,
            cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None,
    ) -> int:
        if cache is None:
            cache = defaultdict(lambda: defaultdict(int))

        # Base case: empty string
        if index1 >= len(text1) or index2 >= len(text2):
            return 0

        if index2 in cache[index1]:
            return cache[index1][index2]

        char1, char2 = text1[index1], text2[index2]

        # If both characters match, we can check for the remainings' subsequence length
        if char1 == char2:
            result = 1 + self.longestCommonSubsequence(text1, text2, index1+1, index2+1, cache)

        # If they don't match, we can't be sure if the current character
        # will matter in either's final count or not. So, we account for
        # both scenarios (check last test case as an example)
        else:
            result = max(
                self.longestCommonSubsequence(text1, text2, index1, index2+1, cache),
                self.longestCommonSubsequence(text1, text2, index1+1, index2, cache),
            )

        cache[index1][index2] = result
        return result


tests = [
    (
        ("abcde", "ace",),
        3,
    ),
    (
        ("abc", "abc",),
        3,
    ),
    (
        ("abc", "def",),
        0,
    ),
    (
        ("abcddrh", "abddghj",),
        5,
    ),
    (
        ("opmtqvejqvudezchsloxizynabehqbyzknunobehkzqtkt",
         "srwbovohkvqhwrwvizebsrszcxepqrenilmvadqxuncpwhe",),
        14,
    ),
]
