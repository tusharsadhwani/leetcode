from collections import defaultdict


# Method 3 - Bottom-up DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache: defaultdict[int, defaultdict[int, int]] = defaultdict(lambda: defaultdict(int))

        # Indices [0] are reserved for empty string cases, for which answer is always zero.
        for index1, char1 in enumerate(text1, start=1):
            for index2, char2 in enumerate(text2, start=1):
                # If both characters match, we can check for the remainings' subsequence length
                if char1 == char2:
                    cache[index1][index2] = 1 + cache[index1-1][index2-1]

                # If they don't match, we can't be sure if the current character
                # will matter in either's final count or not. So, we account for
                # both scenarios (check last test case as an example)
                else:
                    cache[index1][index2] = max(
                        cache[index1][index2-1],
                        cache[index1-1][index2]
                    )

        return cache[len(text1)][len(text2)]


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
