class Solution:
    def replaceDigits(self, string: str) -> str:
        chars = ['' for _ in string]
        for index, char in enumerate(string):
            if index % 2 == 0:
                chars[index] = char
                continue

            offset = int(char)
            chars[index] = chr(ord(chars[index-1]) + offset)

        return ''.join(chars)


tests = [
    (
        ("a1c1e1",),
        "abcdef",
    ),
    (
        ("a1b2c3d4e",),
        "abbdcfdhe",
    ),
]
