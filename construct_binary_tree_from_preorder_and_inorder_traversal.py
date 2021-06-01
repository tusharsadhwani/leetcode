from typing import Callable, Optional
from testutils.trees import TreeNode, build_tree, traverse


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

    tree_values = [node.val for node in traverse(tree)]
    expected_values = [node.val for node in traverse(expected_tree)]
    assert tree_values == expected_values, (tree_values, expected_values)
