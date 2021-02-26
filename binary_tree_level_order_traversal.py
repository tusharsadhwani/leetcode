from collections import deque
from typing import Callable, Deque, Optional


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
