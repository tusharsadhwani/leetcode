from typing import Callable, Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[ListNode] = None

    def __repr__(self) -> str:
        return f'ListNode({self.val})'


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
            # Since fast is always ahead of slow,
            # slow.next is always < fast.next. So we can assume these two.
            assert slow is not None
            assert slow.next is not None

            # Same as doing:
            #     old_prev = prev
            #     prev = slow
            #     slow = slow.next
            #     prev.next = old_prev
            # All this is doing is forwarding both prev and slow 1 step,
            # While also reversing the list behind prev.
            prev, prev.next, slow = slow, prev, slow.next

        # For odd number of elements, prev will be 1 element behind the
        # middle element, while slow will be on the middle element.
        # So we want slow to move 1 element ahead, as middle element
        # is the same for both.
        if fast is not None:
            assert slow is not None
            slow = slow.next

        # Now, we have divided our list into two linked lists,
        # One, moving forwards from slow,
        # Two, moving backwards from prev.
        # All we need to do is confirm both have the same elements.
        while prev is not None:
            assert slow is not None
            if prev.val != slow.val:
                return False

            slow = slow.next
            prev = prev.next

        # Making sure the lengths of the two weren't mismatched.
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
    (
        ([1, 2, 3, 2, 1, 1],),
        False,
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
