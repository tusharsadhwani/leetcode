from collections import Counter

# Naive code, too slow
# class Solution:
#     def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
#         words2_counters = [Counter(word) for word in words2]
#         subsets: list[str] = []
#         for word in words1:
#             is_universal = True
#
#             word_counter = Counter(word)
#             for char_counter in words2_counters:
#                 for char, count in char_counter.items():
#                     if word_counter[char] < count:
#                         is_universal = False
#                         break
#
#                 if not is_universal:
#                     break
#
#             if is_universal:
#                 subsets.append(word)
#
#         return subsets


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        word2_union = Counter('')
        for word in words2:
            for char, count in Counter(word).items():
                if word2_union[char] < count:
                    word2_union[char] = count

        subsets: list[str] = []
        for word in words1:
            word_counter = Counter(word)
            for char, count in word2_union.items():
                if word_counter[char] < count:
                    break

            else:
                subsets.append(word)

        return subsets


tests = [
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"],),
        ["facebook", "google", "leetcode"],
    ),
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]),
        ["apple", "google", "leetcode"],
    ),
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"],),
        ["facebook", "google", ],
    ),
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ['lo', 'eo'],),
        ["google", "leetcode"],
    ),
    (
        (["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"],),
        ["facebook", "leetcode"],
    ),
]
