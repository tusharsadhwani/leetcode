from collections import defaultdict
from typing import MutableMapping


# Solution 3 - Bottom-up DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache: MutableMapping[int, MutableMapping[int, int]] = defaultdict(lambda: defaultdict(int))

        # Initialization
        for index1 in range(1, len(word1)+1):
            cache[index1][0] = index1

        for index2 in range(1, len(word2)+1):
            cache[0][index2] = index2

        for index1, char1 in enumerate(word1, start=1):
            for index2, char2 in enumerate(word2, start=1):
                if char1 == char2:
                    cache[index1][index2] = cache[index1-1][index2-1]
                    continue

                cache[index1][index2] = min(
                    1 + cache[index1-1][index2],
                    1 + cache[index1][index2-1],
                    1 + cache[index1-1][index2-1],
                )

        return cache[len(word1)][len(word2)]


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
