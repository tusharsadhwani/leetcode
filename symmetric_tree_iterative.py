from typing import Callable, Deque, Optional
from collections import deque


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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue: Deque[Optional[TreeNode]] = deque((root, root))

        while len(queue) > 0:
            node1, node2 = queue.popleft(), queue.popleft()
            if node1 is None or node2 is None:
                if node1 != node2:
                    return False

                continue

            if node1.val != node2.val:
                return False

            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node2.left)
            queue.append(node1.right)

        return True


tests = [
    (
        ([1, 2, 2, 3, 4, 4, 3],),
        True,
    ),
    (
        ([1, 2, 2, None, 3, None, 3],),
        False,
    ),
]


def validator(
        isSymmetric: Callable[[Optional[TreeNode]], bool],
        inputs: tuple[list[Optional[int]]],
        expected: bool
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = isSymmetric(tree)
    assert output == expected, (output, expected)
