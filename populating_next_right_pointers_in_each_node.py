from typing import Callable, Deque, Optional
from collections import deque


class Node:
    def __init__(
            self,
            val: int = 0,
            left: Optional['Node'] = None,
            right: Optional['Node'] = None,
            next: Optional['Node'] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return f'Node({self.val!r})'


def build_tree(values: list[Optional[int]]) -> Optional[Node]:
    """Builds tree out of given values"""
    if len(values) == 0:
        return None

    if values[0] is None:
        return None

    root = Node(values[0])
    queue: Deque[Node] = deque()

    current_node = root
    children_assigned = 0
    for num in values[1:]:
        value = None if num is None else Node(num)

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


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None

        if root.left is not None:
            root.left.next = root.right
            assert root.right is not None
            if root.next is not None:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root


tests = [
    (
        ([1, 2, 3, 4, 5, 6, 7],),
        [1, None, 2, 3, None, 4, 5, 6, 7, None]
    ),
]


def validator(
        connect: Callable[[Optional[Node]], Optional[Node]],
        inputs: tuple[list[Optional[int]]],
        expected: None,
) -> None:
    values, = inputs
    tree = build_tree(values)
    connect(tree)
    output: list[Optional[int]] = []
    while tree is not None:
        output.append(tree.val)
        node = tree.next
        while node:
            output.append(node.val)
            node = node.next
        output.append(None)
        tree = tree.left

    assert output == expected, (output, expected)


s = Solution()
s.connect(build_tree([1, 2, 3, 4, 5, 6, 7]))
