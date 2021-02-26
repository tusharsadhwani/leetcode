from itertools import zip_longest
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
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        return TreeNode(1)


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
    input_levels = levels(tree)
    expected_levels = levels(output_tree)

    height = len(input_levels)
    expected_height = len(expected_levels)
    assert height == expected_height, (height, expected_height)

    for l1, l2 in zip(input_levels, expected_levels):
        values, expected = set(l1), set(l2)
        assert values == expected, (values, expected)


def levels(root: Optional[TreeNode]) -> list[list[int]]:
    """Returns levels of a binary tree"""
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
