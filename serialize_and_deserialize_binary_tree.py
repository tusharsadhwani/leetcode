from typing import Deque, Optional
from collections import deque
from testutils.trees import TreeNode, build_tree, traverse


class Solution:
    def dummy(*_: object) -> None: ...


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        items: list[Optional[int]] = []
        queue: Deque[Optional[TreeNode]] = deque()
        queue.append(root)

        while queue:
            item = queue.popleft()
            items.append(None if item is None else item.val)

            if item is not None:
                queue.append(item.left)
                queue.append(item.right)

        items_str = ['' if item is None else str(item) for item in items]
        return ','.join(items_str)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        items_str = data.split(',')
        items = [None if item == "" else int(item) for item in items_str]

        if len(items) == 0:
            return None

        if items[0] is None:
            return None

        root = TreeNode(items[0])
        queue: Deque[TreeNode] = deque()

        current_node = root
        children_assigned = 0
        for num in items[1:]:
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


tests = [
    (
        ([1, 2, 3, None, None, 4, 5],),
        [1, 2, 3, None, None, 4, 5],
    ),
    (
        ([],),
        [],
    ),
    (
        ([1],),
        [1],
    ),
    (
        ([1, 2],),
        [1, 2],
    ),
]


def validator(
        _: object,
        inputs: tuple[list[Optional[int]]],
        expected: list[Optional[int]],
) -> None:
    values, = inputs
    tree = build_tree(values)

    codec = Codec()
    output_tree = codec.deserialize(codec.serialize(tree))
    expected_tree = build_tree(expected)

    tree_values = [node.val for node in traverse(output_tree)]
    expected_values = [node.val for node in traverse(expected_tree)]
    assert tree_values == expected_values, (tree_values, expected_values)
