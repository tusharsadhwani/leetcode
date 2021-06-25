from collections import defaultdict


# Printing the largest subsequence using the alt-Solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
        cache: defaultdict[int, defaultdict[int, str]] = defaultdict(lambda: defaultdict(str))

        for index1, char1 in enumerate(text1, start=1):
            for index2, char2 in enumerate(text2, start=1):
                if char1 == char2:
                    cache[index1][index2] = cache[index1-1][index2-1] + char1

                else:
                    cache[index1][index2] = max(
                        cache[index1][index2-1],
                        cache[index1-1][index2],
                        key=len,  # Important
                    )

        return cache[len(text1)][len(text2)]


tests = [
    (
        ("abcde", "ace",),
        "ace",
    ),
    (
        ("abc", "abc",),
        "abc",
    ),
    (
        ("abc", "def",),
        "",
    ),
    (
        ("abcddrh", "abddghj",),
        "abddh",
    ),
    (
        ("opmtqvejqvudezchsloxizynabehqbyzknunobehkzqtkt",
         "srwbovohkvqhwrwvizebsrszcxepqrenilmvadqxuncpwhe",),
        "ovqvezcxeqnunh",
    ),
]
