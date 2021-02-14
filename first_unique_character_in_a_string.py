class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_indices = [-1] * 26
        repeats = [False] * len(s)

        for index, char in enumerate(s):
            char_index = ord(char) - ord('a')

            first_index = first_indices[char_index]
            if first_index >= 0:
                repeats[first_index] = True
                repeats[index] = True
            else:
                first_indices[char_index] = index

        for index, char in enumerate(s):
            char_index = ord(char) - ord('a')
            first_index = first_indices[char_index]
            repeated = repeats[first_index]
            if not repeated:
                return index

        return -1


tests = [
    (
        ("leetcode",),
        0,
    ),
    (
        ("loveleetcode",),
        2,
    ),
]
