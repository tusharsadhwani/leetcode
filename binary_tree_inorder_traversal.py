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
        ([1, None, 2, None, None, 3],),
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
