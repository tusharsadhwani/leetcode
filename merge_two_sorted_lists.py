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


class Solution:
    def mergeTwoLists(
            self, l1: Optional[ListNode],
            l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        new_list = head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next

            new_list = new_list.next

        while l1 is not None:
            new_list.next = l1
            new_list = new_list.next
            l1 = l1.next

        while l2 is not None:
            new_list.next = l2
            new_list = new_list.next
            l2 = l2.next

        return head


tests = [
    (
        ([1, 2, 4], [1, 3, 4],),
        [1, 1, 2, 3, 4, 4],
    ),
    (
        ([], [0]),
        [0],
    ),
]


def validator(
        mergeTwoLists: Callable[
            [Optional[ListNode], Optional[ListNode]],
            Optional[ListNode]
        ],
        inputs: tuple[list[int], list[int]],
        expected: list[int]
) -> None:
    values1, values2 = inputs
    node_list1 = create_node_list(values1) if len(values1) > 0 else None
    node_list2 = create_node_list(values2) if len(values2) > 0 else None
    new_list = mergeTwoLists(node_list1, node_list2)

    list_values = get_values(new_list) if new_list is not None else []
    assert list_values == expected, (list_values, expected)
