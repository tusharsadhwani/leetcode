class Solution:
    def partition(self, s: str) -> list[list[str]]:
        if len(s) == 0:
            return [[]]

        result = []

        def backtrack(current: list[str], prefix: str) -> None:
            if len(prefix) == 0:
                result.append(current)
                return

            for index in range(1, len(prefix)+1):
                substring = prefix[:index]
                if substring == substring[::-1]:
                    backtrack(current + [substring], prefix[index:])

        backtrack([], s)

        return result


tests = [
    (
        ("aab",),
        [["a", "a", "b"], ["aa", "b"]],
    ),
    (
        ("a",),
        [["a"]],
    ),
]
