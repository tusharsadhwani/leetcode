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
