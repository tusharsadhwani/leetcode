def generate_parenthesis_recursive(
        paren_list: list[str],
        max_parens: int,
        parens: str = '',
        left_count: int = 0,
        right_count: int = 0
) -> None:
    if len(parens) == 2 * max_parens:
        paren_list.append(parens)
        return

    if left_count < max_parens:
        generate_parenthesis_recursive(
            paren_list,
            max_parens,
            parens + '(',
            left_count + 1,
            right_count
        )
    if right_count < left_count:
        generate_parenthesis_recursive(
            paren_list,
            max_parens,
            parens + ')',
            left_count,
            right_count + 1
        )


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        paren_list: list[str] = []
        generate_parenthesis_recursive(paren_list, n)
        return paren_list


tests = [
    (
        (3,),
        ["((()))", "(()())", "(())()", "()(())", "()()()"],
    ),
    (
        (1,),
        ["()"],
    ),
]
