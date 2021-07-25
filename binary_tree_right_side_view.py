from typing import Callable, Generator, Optional

from testutils.trees import TreeNode, build_tree


def prerder_traversal(
        root: Optional[TreeNode],
        level: int = 0,
) -> Generator[tuple[TreeNode, int], None, None]:
    """Traverses the tree in preorder"""
    if root is None:
        return

    yield root, level
    yield from prerder_traversal(root.left, level=level+1)
    yield from prerder_traversal(root.right, level=level+1)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        # Approach:
        # In both in-order and pre-order traversal, the right nodes are
        # visited last. Because of this, we can be sure that the last
        # node visited per level in those travsersals is the rightmost.
        right_nodes: list[int] = []
        for node, level in prerder_traversal(root):
            if level == len(right_nodes):
                right_nodes.append(node.val)
            else:
                right_nodes[level] = node.val

        return right_nodes


tests = [
    (
        ([1, 2, 3, None, 5, None, 4],),
        [1, 3, 4],
    ),
    (
        ([1, None, 3],),
        [1, 3],
    ),
    (
        ([],),
        [],
    ),
]


def validator(
        rightSideView: Callable[[Optional[TreeNode]], list[int]],
        inputs: tuple[list[Optional[int]]],
        expected: list[int],
) -> None:
    nums, = inputs
    root = build_tree(nums)

    output = rightSideView(root)
    assert output == expected, (output, expected)
