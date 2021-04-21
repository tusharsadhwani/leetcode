from typing import Callable, Optional
from utils.trees import TreeNode, build_tree


def max_depth_recursive(root: Optional[TreeNode], depth: int = 0) -> int:
    """Recursive max depth of tree implementation"""
    if root is None:
        return depth

    return max(
        max_depth_recursive(root.left, depth+1),
        max_depth_recursive(root.right, depth+1),
    )


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth_recursive(root)


tests = [
    (
        ([3, 9, 20, None, None, 15, 7],),
        3,
    ),
    (
        ([1, None, 2],),
        2,
    ),
    (
        ([],),
        0,
    ),
    (
        ([0],),
        1,
    ),
]


def validator(
        maxDepth: Callable[[Optional[TreeNode]], int],
        inputs: tuple[list[Optional[int]]],
        expected: int
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = maxDepth(tree)
    assert output == expected, (output, expected)
