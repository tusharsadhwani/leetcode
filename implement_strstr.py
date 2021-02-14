class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        offset_length = len(haystack) - len(needle) + 1
        if offset_length == 0:
            return 0 if needle == haystack else -1

        for offset in range(offset_length):
            for index, char in enumerate(needle):
                haystack_char = haystack[offset + index]
                if char != haystack_char:
                    break
            else:
                return offset

        return -1


tests = [
    (
        ("hello", "ll",),
        2,
    ),
    (
        ("aaaaa", "bba",),
        -1,
    ),
    (
        ("", "",),
        0,
    ),
    (
        ("abc", "c",),
        2,
    ),
]
