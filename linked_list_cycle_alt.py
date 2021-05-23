from typing import Callable, Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        node: Optional[ListNode] = head
        while node is not None:
            if node in seen:
                return True

            seen.add(node)
            node = node.next

        return False


def create_cyclic_node_list(values: list[int], pos: int) -> ListNode:
    """Creates a potentially cyclic ListNode out of a list of values"""
    current = 0
    head = ListNode(values[0])

    cycle_node: Optional[ListNode] = None

    last_node = head
    for value in values[1:]:
        node = ListNode(value)
        if current == pos:
            cycle_node = node

        last_node.next = node
        last_node = node
        current += 1

    if cycle_node:
        last_node.next = cycle_node

    return head


tests = [
    (
        ([3, 2, 0, -4], 1,),
        True
    ),
    (
        ([1, 2], 0,),
        True,
    ),
    (
        ([1], -1,),
        False,
    ),
]


def validator(
        hasCycle: Callable[[ListNode], bool],
        inputs: tuple[list[int], int],
        expected: bool
) -> None:
    values, pos = inputs
    node_list = create_cyclic_node_list(values, pos)
    output = hasCycle(node_list)

    assert output == expected, (output, expected)
