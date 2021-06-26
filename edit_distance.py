# # Solution 1 - Recursion
# class Solution:
#     def minDistance(
#             self,
#             word1: str,
#             word2: str,
#             index1: int = 0,
#             index2: int = 0,
#     ) -> int:
#         # Base cases
#         if index1 >= len(word1):
#             return len(word2) - index2

#         if index2 >= len(word2):
#             return len(word1) - index1

#         char1 = word1[index1]
#         char2 = word2[index2]

#         if char1 == char2:
#             return self.minDistance(word1, word2, index1+1, index2+1)

#         # We're going from word1 to word2, and we have 3 options:
#         return min(
#             # Delete char1
#             1 + self.minDistance(word1, word2, index1+1, index2),
#             # Insert char2, which is kindof like deleting char2
#             1 + self.minDistance(word1, word2, index1, index2+1),
#             # Change char1 to char2, which is like deleting both chars
#             1 + self.minDistance(word1, word2, index1+1, index2+1),
#         )


# Solution 2 - Memoization
from collections import defaultdict
from typing import MutableMapping, Optional


class Solution:
    def minDistance(
            self,
            word1: str,
            word2: str,
            index1: int = 0,
            index2: int = 0,
            cache: Optional[MutableMapping[int, MutableMapping[int, int]]] = None,
    ) -> int:
        if cache is None:
            cache = defaultdict(lambda: defaultdict(int))

        # Base cases
        if index1 >= len(word1):
            return len(word2) - index2

        if index2 >= len(word2):
            return len(word1) - index1

        if index2 in cache[index1]:
            return cache[index1][index2]

        char1 = word1[index1]
        char2 = word2[index2]

        if char1 == char2:
            result = self.minDistance(word1, word2, index1+1, index2+1, cache)

        else:
            # We're going from word1 to word2, and we have 3 options:
            result = min(
                # Delete char1
                1 + self.minDistance(word1, word2, index1+1, index2, cache),
                # Insert char2, which is kindof like deleting char2
                1 + self.minDistance(word1, word2, index1, index2+1, cache),
                # Change char1 to char2, which is like deleting both chars
                1 + self.minDistance(word1, word2, index1+1, index2+1, cache),
            )

        cache[index1][index2] = result
        return result


tests = [
    (
        ("horse", "ros",),
        3,
    ),
    (
        ("intention", "execution",),
        5,
    ),
]
