from typing import Callable, Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
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


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        length = 1
        curr = head.next
        while curr is not None:
            length += 1
            curr = curr.next

        if n == length:
            return head.next
        else:
            prev = head
            curr = head.next
            index = length - n - 1
            while index > 0:
                assert curr is not None
                prev = curr
                curr = curr.next
                index -= 1

            assert curr is not None
            prev.next = curr.next

        return head


tests = [
    (
        ([1, 2, 3, 4, 5], 2,),
        [1, 2, 3, 5],
    ),
    (
        ([1], 1,),
        [],
    ),
    (
        ([1, 2], 1,),
        [1],
    ),
]


def validator(
        removeNthFromEnd: Callable[[ListNode, int], Optional[ListNode]],
        inputs: tuple[list[int], int],
        expected: list[int]
) -> None:
    values, index = inputs
    node_list = create_node_list(values)
    new_list = removeNthFromEnd(node_list, index)

    list_values = get_values(new_list) if new_list is not None else []
    assert list_values == expected, (list_values, expected)
