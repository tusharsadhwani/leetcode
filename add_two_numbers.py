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
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head: Optional[ListNode] = None
        digit_node = head
        while l1 is not None or l2 is not None:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            digit_sum = digit1 + digit2 + carry
            digit_sum, carry = digit_sum % 10, digit_sum // 10
            new_node = ListNode(digit_sum)

            if digit_node is None:
                digit_node = new_node
                head = new_node
            else:
                digit_node.next = new_node
                digit_node = digit_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            assert digit_node is not None
            digit_node.next = ListNode(carry)

        return head


tests = [
    (
        ([2, 4, 3], [5, 6, 4],),
        [7, 0, 8],
    ),
    (
        ([0], [0],),
        [0],
    ),
    (
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9],),
        [8, 9, 9, 9, 0, 0, 0, 1],
    ),
]


def validator(
        addTwoNumbers: Callable[
            [Optional[ListNode], Optional[ListNode]],
            Optional[ListNode]
        ],
        inputs: tuple[list[int], list[int]],
        expected: list[int]
) -> None:
    values1, values2 = inputs
    node_list1 = create_node_list(values1) if len(values1) > 0 else None
    node_list2 = create_node_list(values2) if len(values2) > 0 else None
    new_list = addTwoNumbers(node_list1, node_list2)

    list_values = get_values(new_list) if new_list is not None else []
    assert list_values == expected, (list_values, expected)
