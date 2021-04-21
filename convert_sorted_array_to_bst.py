from typing import Callable, Generator, Optional
from testutils.trees import TreeNode, build_tree


def make_bst(
        nums: list[int],
        start: Optional[int] = None,
        end: Optional[int] = None,
) -> Optional[TreeNode]:
    """Recursively converts a sorted array into a binary search tree"""
    if start is None:
        start = 0
    if end is None:
        end = len(nums) - 1

    if start > end:
        return None

    mid = (start + end) // 2
    value = nums[mid]
    node = TreeNode(value)

    node.left = make_bst(nums, start, mid-1)
    node.right = make_bst(nums, mid+1, end)

    return node


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        return make_bst(nums)


tests = [
    (
        ([-10, -3, 0, 5, 9],),
        [0, -3, 9, -10, None, 5],
    ),
    (
        ([1, 3],),
        [3, 1],
    ),
]


def validator(
        sortedArrayToBST: Callable[[list[int]], Optional[TreeNode]],
        inputs: tuple[list[int]],
        output: list[Optional[int]],
) -> None:
    nums, = inputs
    tree = sortedArrayToBST(nums)
    output_tree = build_tree(output)
    height = max_depth(tree)
    expected_height = max_depth(output_tree)
    assert height == expected_height, (height, expected_height)

    values = list(inorder(tree))
    expected_values = list(inorder(output_tree))
    assert values == expected_values, (values, expected_values)


def max_depth(root: Optional[TreeNode], depth: int = 0) -> int:
    """Recursive max depth of tree implementation"""
    if root is None:
        return depth

    return max(
        max_depth(root.left, depth + 1),
        max_depth(root.right, depth + 1),
    )


def inorder(root: Optional[TreeNode]) -> Generator[int, None, None]:
    """Return tree values in inorder"""
    if root is None:
        return

    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)
