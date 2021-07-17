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


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev: Optional[ListNode] = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            assert slow is not None
            assert slow.next is not None
            prev, prev.next, slow = slow, prev, slow.next

        if fast is not None:
            assert slow is not None
            slow = slow.next

        while prev is not None:
            assert slow is not None
            if prev.val == slow.val:
                slow = slow.next
                prev = prev.next
            else:
                break

        return prev is None


tests = [
    (
        ([1],),
        True,
    ),
    (
        ([1, 2],),
        False,
    ),
    (
        ([1, 2, 2, 1],),
        True,
    ),
    (
        ([1, 2, 3, 4, 5],),
        False,
    ),
    (
        ([1, 2, 3, 2, 1],),
        True,
    ),

]


def validator(
        isPalindrome: Callable[[ListNode], bool],
        inputs: tuple[list[int]],
        expected: bool
) -> None:
    values, = inputs
    node_list = create_node_list(values)
    output = isPalindrome(node_list)
    assert output == expected, (output, expected)
