from typing import Callable, Optional
from testutils.trees import TreeNode, build_tree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        values: list[int] = []

        stack: list[TreeNode] = []
        current: Optional[TreeNode] = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:
                node = stack.pop()
                values.append(node.val)
                current = node.right

            else:
                break

        return values


tests = [
    (
        ([1, None, 2, 3],),
        [1, 3, 2],
    ),
    (
        ([],),
        [],
    ),
    (
        ([1],),
        [1],
    ),
    (
        ([1, 2],),
        [2, 1],
    ),
    (
        ([1, None, 2],),
        [1, 2],
    ),
]


def validator(
        inorderTraversal: Callable[[Optional[TreeNode]], list[int]],
        inputs: tuple[list[Optional[int]]],
        expected: list[int],
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = inorderTraversal(tree)
    assert output == expected, (output, expected)
