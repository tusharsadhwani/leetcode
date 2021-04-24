import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for char in columnTitle:
            total = total * 26 + (1 + string.ascii_uppercase.index(char))
        return total


tests = [
    (
        ('A',),
        1,
    ),
    (
        ('AB',),
        28,
    ),
    (
        ('ZY',),
        701,
    ),
    (
        ('FXSHRXW',),
        2147483647,
    ),
]
