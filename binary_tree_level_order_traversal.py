from typing import Callable, Optional
from utils.trees import TreeNode, build_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        values: list[list[int]] = []
        level = [root]
        while len(level) > 0:
            values.append([node.val for node in level])

            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            level = new_level

        return values


tests = [
    (
        ([3, 9, 20, None, None, 15, 7],),
        [[3], [9, 20], [15, 7]],
    ),
    (
        ([1],),
        [[1]],
    ),
    (
        ([],),
        [],
    ),
    (
        ([3, None, 20, 15, 7],),
        [[3], [20], [15, 7]],
    ),
]


def validator(
        levelOrder: Callable[[Optional[TreeNode]], list[list[int]]],
        inputs: tuple[list[Optional[int]]],
        expected: list[list[int]],
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = levelOrder(tree)
    assert output == expected, (output, expected)
