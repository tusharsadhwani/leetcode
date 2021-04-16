from typing import Callable, Generator, Optional


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
    def buildTree(
            self,
            preorder: list[int],
            inorder: list[int],
    ) -> Optional[TreeNode]:
        if len(preorder) != len(inorder):
            raise ValueError('preorder and inorder length mismatch')

        inorder_indices = {value: index
                           for index, value in enumerate(inorder)}

        preorder_index = 0

        def buildTree_rec(start: int, end: int) -> Optional[TreeNode]:
            """Recursive implementation for buildTree"""
            if start > end:
                return None

            nonlocal preorder_index
            node = TreeNode(preorder[preorder_index])
            preorder_index += 1

            node_inorder_index = inorder_indices[node.val]
            node.left = buildTree_rec(start, node_inorder_index-1)
            node.right = buildTree_rec(node_inorder_index+1, end)

            return node

        node = buildTree_rec(0, len(preorder) - 1)
        return node


tests = [
    (
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7],),
        [3, 9, 20, None, None, 15, 7],
    ),
    (
        ([-1], [-1],),
        [-1],
    ),
]


def validator(
        buildTree: Callable[[list[int], list[int]], Optional[TreeNode]],
        inputs: tuple[list[int], list[int]],
        expected: list[Optional[int]],
) -> None:
    preorder, inorder = inputs
    tree = buildTree(preorder, inorder)
    expected_tree = build_tree(expected)

    tree_values = list(traverse(tree))
    expected_values = list(traverse(expected_tree))
    assert tree_values == expected_values, (tree_values, expected_values)


def traverse(root: Optional[TreeNode]) -> Generator[int, None, None]:
    """Return tree values in inorder"""
    if root is None:
        return

    yield from traverse(root.left)
    yield root.val
    yield from traverse(root.right)