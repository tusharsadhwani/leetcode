from collections import defaultdict
from typing import Any, Optional


class TreeNode:
    def __init__(
            self, val: int,
            left: Optional['TreeNode'] = None,
            right: Optional['TreeNode'] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        trees: defaultdict[tuple[Any, ...], list[TreeNode]] = defaultdict(list)

        def preorder(root: Optional[TreeNode]) -> Optional[tuple[Any, ...]]:
            if root is None:
                return None

            # this is a nested tuple of tuples that represents the whole subtree
            preorder_tuple = (root.val, preorder(root.left), preorder(root.right))
            trees[preorder_tuple].append(root)
            return preorder_tuple

        preorder(root)
        return [nodes[0] for nodes in trees.values() if len(nodes) > 1]


# TODO: write tests
