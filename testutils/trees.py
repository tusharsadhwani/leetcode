from collections import deque
from typing import Deque, Generator, Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f'TreeNode({self.val})'


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Builds tree out of given values"""
    if len(values) == 0:
        return None

    if values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: Deque[TreeNode] = deque()

    current_node = root
    children_assigned = 0
    for num in values[1:]:
        value = None if num is None else TreeNode(num)

        if children_assigned == 2:
            current_node = queue.popleft()
            children_assigned = 0

        if children_assigned == 0:
            current_node.left = value

        elif children_assigned == 1:
            current_node.right = value

        if value is not None:
            queue.append(value)

        children_assigned += 1

    return root


def traverse(node: Optional[TreeNode]) -> Generator[TreeNode, None, None]:
    """Return tree values in inorder"""
    if node is None:
        return

    yield from traverse(node.left)
    yield node
    yield from traverse(node.right)


def find(root: TreeNode, value: int) -> TreeNode:
    """Returns the node with given value"""
    for node in traverse(root):
        if node.val == value:
            return node

    raise ValueError('Node not found')
