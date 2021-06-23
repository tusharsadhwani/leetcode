from collections import defaultdict


# Printing the largest subsequence using the alt-Solution, without storing strings
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache: defaultdict[int, defaultdict[int, int]] = defaultdict(lambda: defaultdict(int))

        for index1, char1 in enumerate(text1, start=1):
            for index2, char2 in enumerate(text2, start=1):
                if char1 == char2:
                    cache[index1][index2] = 1 + cache[index1-1][index2-1]

                else:
                    cache[index1][index2] = max(
                        cache[index1][index2-1],
                        cache[index1-1][index2],
                    )

        # Now the trick is to back-track through the DP values.
        # If we find indices where the character matches, we add it to our answer,
        # and go diagonally towards index (i-1, j-1).
        # Otherwise, we follow backwards towards the larger of the two adjacent values.
        answer_reverse = ''
        index1, index2 = len(text1), len(text2)
        while index1 > 0 and index2 > 0:
            # Since cache indices go from 1 to N instead of 0 to N-1, we have to subtract 1
            if text1[index1-1] == text2[index2-1]:
                answer_reverse += text1[index1-1]
                index1 -= 1
                index2 -= 1
            else:
                if cache[index1-1][index2] > cache[index1][index2-1]:
                    index1 -= 1
                else:
                    index2 -= 1

        return answer_reverse[::-1]


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
