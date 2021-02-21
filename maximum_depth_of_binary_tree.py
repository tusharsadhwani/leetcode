from typing import Callable, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def build_tree(
        values: list[Optional[int]],
        index: int = 0
) -> Optional[TreeNode]:
    """Builds tree out of given values"""
    length = len(values)
    if index >= length:
        return None

    value = values[index]
    if value is None:
        return None

    node = TreeNode(value)
    node.left = build_tree(values, 2*index + 1)
    node.right = build_tree(values, 2*index + 2)

    return node


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
        expected: bool
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = maxDepth(tree)
    assert output == expected, (output, expected)
