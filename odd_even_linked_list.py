from typing import Callable, Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[ListNode] = None

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.val})'


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


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        last_odd_node = head
        last_even_node: Optional[ListNode] = head.next
        next_odd_node = head.next.next

        while next_odd_node is not None:
            first_even_node = last_odd_node.next

            assert first_even_node is not None
            assert last_even_node is not None

            last_odd_node.next = next_odd_node
            last_even_node.next = next_odd_node.next
            next_odd_node.next = first_even_node

            last_odd_node = next_odd_node
            last_even_node = last_even_node.next
            next_odd_node = (
                last_even_node.next
                if last_even_node is not None
                else None
            )

        return head


tests = [
    (
        ([1, 2, 3, 4, 5],),
        [1, 3, 5, 2, 4],
    ),
    (
        ([2, 1, 3, 5, 6, 4, 7],),
        [2, 3, 6, 7, 1, 5, 4],
    ),
]


def validator(
        addTwoNumbers: Callable[[Optional[ListNode]], Optional[ListNode]],
        inputs: tuple[list[int]],
        expected: list[int]
) -> None:
    values, = inputs
    node_list = create_node_list(values) if len(values) > 0 else None
    new_list = addTwoNumbers(node_list)

    list_values = get_values(new_list) if new_list is not None else []
    assert list_values == expected, (list_values, expected)
