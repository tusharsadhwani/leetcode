from typing import Callable, Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Optional[ListNode] = None


def create_node_list(values: list[int], val: int) -> tuple[ListNode, ListNode]:
    """Creates a ListNode out of a list of values"""
    head = ListNode(values[0])
    return_node = head

    last_node = head
    for value in values[1:]:
        node = ListNode(value)
        if node.val == val:
            return_node = node

        last_node.next = node
        last_node = node

    return head, return_node


def get_values(node: ListNode) -> list[int]:
    """Returns the values in linked list"""
    values = [node.val]
    curr = node.next
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        assert node.next is not None, (node.next, None)
        node.val = node.next.val
        node.next = node.next.next


tests = [
    (
        ([4, 5, 1, 9], 5,),
        [4, 1, 9],
    ),
    (
        ([4, 5, 1, 9], 1,),
        [4, 5, 9],
    ),
    (
        ([1, 2, 3, 4], 3,),
        [1, 2, 4],
    ),
    (
        ([0, 1], 0,),
        [1],
    ),
    (
        ([-3, 5, -99], -3,),
        [5, -99],
    ),
]


def validator(
        deleteNode: Callable[[ListNode], None],
        inputs: tuple[list[int], int],
        expected: list[int]
) -> None:
    values, node_value = inputs
    node_list, node = create_node_list(values, node_value)
    deleteNode(node)

    list_values = get_values(node_list)
    assert list_values == expected, (list_values, expected)
