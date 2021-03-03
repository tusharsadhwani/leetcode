class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        start, stop = 0, 0
        end = len(s)

        max_length = 0
        chars: dict[str, int] = {}
        while start <= stop < end:
            new_char = s[stop]
            if new_char in chars:
                start = max(start, chars[new_char] + 1)

            chars[new_char] = stop

            length = stop - start + 1
            max_length = max(max_length, length)

            stop += 1

        return max_length


tests = [
    (
        ("abcabcbb",),
        3,
    ),
    (
        ("bbbbb",),
        1,
    ),
    (
        ("pwwkew",),
        3,
    ),
    (
        ("",),
        0,
    ),
    (
        ("a",),
        1,
    ),
    (
        ("abcde",),
        5,
    ),
    (
        ("abba",),
        2,
    ),
]
