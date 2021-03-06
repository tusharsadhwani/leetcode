from typing import Callable, Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[ListNode] = None


def create_node_list(values: list[int]) -> ListNode:
    """Creates a ListNode out of a list of values"""
    head = ListNode(values[0])

    last_node = head
    for value in values[1:]:
        node = ListNode(value)
        last_node.next = node
        last_node = node

    return head


def get_values(node: ListNode) -> list[int]:
    """Returns the values in linked list"""
    values = [node.val]
    curr = node.next
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values


def reverse_ll(head: ListNode) -> tuple[ListNode, ListNode]:
    if head.next is None:
        return head, head

    new_head, new_tail = reverse_ll(head.next)
    new_tail.next = head
    head.next = None
    return new_head, head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head, _ = reverse_ll(head)
        return new_head


tests = [
    (
        ([1, 2, 3, 4, 5],),
        [5, 4, 3, 2, 1],
    ),
    (
        ([],),
        [],
    ),
]


def validator(
        reverseList: Callable[[Optional[ListNode]], Optional[ListNode]],
        inputs: tuple[list[int]],
        expected: list[int]
) -> None:
    values, = inputs
    node_list = create_node_list(values) if len(values) > 0 else None
    new_list = reverseList(node_list)

    list_values = get_values(new_list) if new_list is not None else []
    assert list_values == expected, (list_values, expected)
