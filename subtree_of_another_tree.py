from typing import Callable, Optional
from testutils.trees import TreeNode, build_tree


def preorder_string(node: Optional[TreeNode]) -> str:
    """Returns a uniquely identifyable preorder string of the tree"""
    if not node:
        return ''

    return f"# {node.val} {preorder_string(node.left)} {preorder_string(node.right)}"


class Solution:
    def isSubtree(self, tree: Optional[TreeNode], subtree: Optional[TreeNode]) -> bool:
        return preorder_string(subtree) in preorder_string(tree)


tests = [
    (
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2],),
        False,
    ),
    (
        ([3, 4, 5, 1, 2], [4, 1, 2],),
        True,
    ),
]


def validator(
        isSubtree: Callable[[Optional[TreeNode], Optional[TreeNode]], bool],
        inputs: tuple[list[Optional[int]], list[Optional[int]]],
        expected: bool,
) -> None:
    tree_vals, subtree_vals = inputs
    tree = build_tree(tree_vals)
    subtree = build_tree(subtree_vals)

    output = isSubtree(tree, subtree)
    assert output == expected, (output, expected)
