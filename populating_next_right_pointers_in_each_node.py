from typing import Callable, Optional


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


def build_tree(
        values: list[Optional[int]],
        index: int = 0
) -> Optional[Node]:
    """Builds tree out of given values"""
    length = len(values)
    if index >= length:
        return None

    value = values[index]
    if value is None:
        return None

    node = Node(value)
    node.left = build_tree(values, 2*index + 1)
    node.right = build_tree(values, 2*index + 2)

    return node


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
