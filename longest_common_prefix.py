class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ''

        first_str = strs[0]
        index = 0
        for chars in zip(*strs):
            if not all(char == chars[0] for char in chars):
                break
            index += 1

        return first_str[:index]


tests = [
    (
        (["flower", "flow", "flight"],),
        "fl",
    ),
    (
        (["dog", "racecar", "car"],),
        "",
    ),
]
