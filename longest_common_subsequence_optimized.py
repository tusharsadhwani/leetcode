from collections import defaultdict


# Method 4 - Bottom-up DP, Space Optimized
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache: defaultdict[int, int] = defaultdict(int)

        for char1 in text1:
            prev_cache = cache.copy()
            for index2, char2 in enumerate(text2, start=1):
                # Since we only access indices index1-1 and index2-1,
                # we can get away with storing just 1 row of old data.

                if char1 == char2:
                    # NOTE: [index1 - 1] replaced with prev_cache
                    cache[index2] = 1 + prev_cache[index2-1]
                else:
                    cache[index2] = max(cache[index2-1], cache[index2])

        return cache[len(text2)]


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
