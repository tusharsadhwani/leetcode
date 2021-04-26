class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers: list[int] = []

        for token in tokens:
            if token not in '+-*/':
                numbers.append(int(token))
                continue

            num2, num1 = numbers.pop(), numbers.pop()  # notice the order
            if token == '+':
                ans = num1 + num2
            elif token == '-':
                ans = num1 - num2
            elif token == '*':
                ans = num1 * num2
            elif token == '/':
                ans = int(num1 / num2)

            numbers.append(ans)

        return numbers.pop()


tests = [
    (
        (["4", "13", "5", "/", "+"],),
        6,
    ),
    (
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],),
        22,
    ),
]
