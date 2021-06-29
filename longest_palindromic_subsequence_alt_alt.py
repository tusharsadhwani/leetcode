# Method 5 - LCS
def lcs(text1: str, text2: str) -> int:
    cache: list[int] = [0 for _ in range(len(text2)+1)]

    for char1 in text1:
        prev_cache = cache.copy()
        for index2, char2 in enumerate(text2, start=1):
            if char1 == char2:
                cache[index2] = 1 + prev_cache[index2-1]
            else:
                cache[index2] = max(cache[index2-1], cache[index2])

    return cache[-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return lcs(s, s[::-1])


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
