from typing import Callable, Generator, Optional
from testutils.trees import TreeNode, build_tree


def inorder_traversal(root: TreeNode) -> Generator[int, None, None]:
    stack: list[TreeNode] = []
    current: Optional[TreeNode] = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif stack:
            node = stack.pop()
            yield node.val
            current = node.right

        else:
            break


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        counter = 1
        for value in inorder_traversal(root):
            if counter == k:
                return value

            counter += 1

        return -1


tests = [
    (
        ([3, 1, 4, None, 2], 1,),
        1,
    ),
    (
        ([5, 3, 6, 2, 4, None, None, 1], 3,),
        3,
    ),
]


def validator(
        kthSmallest: Callable[[Optional[TreeNode], int], int],
        inputs: tuple[list[Optional[int]], int],
        expected: int,
) -> None:
    values, k = inputs
    tree = build_tree(values)
    output = kthSmallest(tree, k)
    assert output == expected, (output, expected)
