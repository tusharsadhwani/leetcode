from typing import Callable, Optional
from testutils.trees import TreeNode, build_tree


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        ans: list[list[int]] = []
        level = [root]

        reverse = False
        while len(level) > 0:
            values = [node.val for node in level]
            ans.append(values[::-1] if reverse else values)

            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            level = new_level
            reverse = not reverse

        return ans


tests = [
    (
        ([3, 9, 20, None, None, 15, 7],),
        [[3], [20, 9], [15, 7]],
    ),
    (
        ([1],),
        [[1]],
    ),
    (
        ([],),
        [],
    ),
]


def validator(
        zigzagLevelOrder: Callable[[Optional[TreeNode]], list[list[int]]],
        inputs: tuple[list[Optional[int]]],
        expected: list[list[int]],
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = zigzagLevelOrder(tree)
    assert output == expected, (output, expected)
