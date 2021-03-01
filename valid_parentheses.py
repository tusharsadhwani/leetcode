class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for char in s:
            if char in '([{':
                stack.append(char)
                continue

            if char == ')':
                if len(stack) < 1 or stack[-1] != '(':
                    return False
                stack.pop()
            elif char == ']':
                if len(stack) < 1 or stack[-1] != '[':
                    return False
                stack.pop()
            elif char == '}':
                if len(stack) < 1 or stack[-1] != '{':
                    return False
                stack.pop()

        return len(stack) == 0


tests = [
    (
        ("()",),
        True,
    ),
    (
        ("()[]{}",),
        True,
    ),
    (
        ("(]",),
        False,
    ),
    (
        ("([)]",),
        False,
    ),
    (
        ("{[]}",),
        True,
    ),
]
