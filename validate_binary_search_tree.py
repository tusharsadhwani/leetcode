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


class Solution:
    def isValidBST(
            self,
            root: Optional[TreeNode],
            min_val: Optional[int] = None,
            max_val: Optional[int] = None,
    ) -> bool:
        if root is None:
            return True

        if min_val and root.val <= min_val:
            return False

        if max_val and root.val >= max_val:
            return False

        if root.left is not None:
            if root.left.val >= root.val:
                return False

            if not self.isValidBST(root.left, min_val, root.val):
                return False

        if root.right is not None:
            if root.right.val <= root.val:
                return False

            if not self.isValidBST(root.right, root.val, max_val):
                return False

        return True


tests = [
    (
        ([2, 1, 3],),
        True,
    ),
    (
        ([5, 1, 4, None, None, 3, 6],),
        False,
    ),
]


def validator(
        isValidBST: Callable[[Optional[TreeNode]], bool],
        inputs: tuple[list[Optional[int]]],
        expected: bool
) -> None:
    values, = inputs
    tree = build_tree(values)
    output = isValidBST(tree)
    assert output == expected, (output, expected)
