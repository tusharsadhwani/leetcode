combos = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(combos[digits[0]])
        return [char + rest
                for char in combos[digits[0]]
                for rest in self.letterCombinations(digits[1:])]


tests = [
    (
        ("23",),
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    ),
    (
        ("",),
        [],
    ),
    (
        ("2",),
        ["a", "b", "c"],
    ),
]
