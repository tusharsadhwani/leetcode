from typing import Callable, Optional
from testutils.trees import TreeNode, build_tree


def is_mirror(
        tree1: Optional[TreeNode],
        tree2: Optional[TreeNode]
) -> bool:
    """Returns if tree1 is a mirror of tree2"""
    if tree1 is None or tree2 is None:
        return tree1 == tree2

    return (
        tree1.val == tree2.val
        and is_mirror(tree1.left, tree2.right)
        and is_mirror(tree2.left, tree1.right)
    )


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return is_mirror(root.left, root.right)


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
