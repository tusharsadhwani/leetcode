# Solution 4 - Bottom-up DP, Space Optimized
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Instead of [index1], you use cache
        # Instead of [index1-1], you use prev_cache

        # First row initialization
        prev_cache = [index2 for index2 in range(len(word2)+1)]

        for index1, char1 in enumerate(word1, start=1):
            # First column initialization
            cache = [0 for _ in range(len(word2)+1)]
            cache[0] = index1

            for index2, char2 in enumerate(word2, start=1):
                if char1 == char2:
                    cache[index2] = prev_cache[index2-1]
                    continue

                # Take the 1 outside the min
                cache[index2] = 1 + min(prev_cache[index2], cache[index2-1], prev_cache[index2-1])

            # Don't forget to set the current row as previous row
            prev_cache = cache

        return prev_cache[-1]


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
