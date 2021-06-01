from typing import Callable, Optional
from testutils.trees import TreeNode, build_tree, find


def are_descendants(
        root: Optional[TreeNode],
        p: TreeNode,
        q: TreeNode,
) -> tuple[Optional[TreeNode], Optional[TreeNode]]:
    """Returns which one of the two nodes are descendants of this node"""
    # Algorithm:
    # - If the ancestor has already been found, we return both same
    #   values: the ancestor.
    # - If any one of the children are the descendants, return that
    #   child, with None as the other child.
    # - If current node is the ancestor (signified by both return values
    #   being different from each other), return ourselves twice.

    if root is None:
        return None, None

    if root is p:
        return p, None

    if root is q:
        return None, q

    p1, q1 = are_descendants(root.left, p, q)
    p2, q2 = are_descendants(root.right, p, q)

    # Cases: Ancestor was already found below
    if p1 == q1 != None:
        return (p1, p1)
    if p2 == q2 != None:
        return (p2, p2)

    left, right = (p1 or p2, q1 or q2)

    # Case: Found the ancestor
    if left is not None and right is not None:
        return root, root

    return left, right


class Solution:
    def lowestCommonAncestor(
            self,
            root: TreeNode,
            p: TreeNode,
            q: TreeNode,
    ) -> TreeNode:
        left, right = are_descendants(root, p, q)
        result = left or right
        assert result is not None
        return result


tests = [
    (
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1,),
        3,
    ),
    (
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4,),
        5,
    ),
    (
        ([1, 2], 1, 2,),
        1,
    ),
]


def validator(
        lowestCommonAncestor: Callable[[TreeNode, TreeNode, TreeNode], TreeNode],
        inputs: tuple[list[Optional[int]], int, int],
        expected: int,
) -> None:
    nums, p, q = inputs
    tree = build_tree(nums)
    assert tree is not None

    node_p = find(tree, p)
    node_q = find(tree, q)
    ancestor = lowestCommonAncestor(tree, node_p, node_q)
    assert ancestor.val == expected, (ancestor.val, expected)
