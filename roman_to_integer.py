class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        largest_value_so_far = 0
        total = 0
        for rune in reversed(s):
            value = values[rune]
            if value < largest_value_so_far:
                total -= value
            else:
                total += value

            largest_value_so_far = max(largest_value_so_far, value)

        return total


tests = [
    (
        ("III",),
        3,
    ),
    (
        ("IV",),
        4,
    ),
    (
        ("IX",),
        9,
    ),
    (
        ("LVIII",),
        58,
    ),
    (
        ("MCMXCIV",),
        1994,
    ),
]
