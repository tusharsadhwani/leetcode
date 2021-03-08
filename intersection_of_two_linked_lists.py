from typing import Callable, Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[ListNode] = None


def create_node_list(values: list[int]) -> Optional[ListNode]:
    """Creates a ListNode out of a list of values"""
    if len(values) == 0:
        return None

    head = ListNode(values[0])

    last_node = head
    for value in values[1:]:
        node = ListNode(value)
        last_node.next = node
        last_node = node

    return head


def create_intersecting_lists(
        valuesA: list[int],
        valuesB: list[int],
        skipA: int,
        skipB: int,
) -> tuple[Optional[ListNode], Optional[ListNode]]:
    """Creates intersecting linked lists"""
    listA = create_node_list(valuesA)
    listB = create_node_list(valuesB)

    indexA = 0
    nodeA = listA
    intersecting_node: Optional[ListNode] = None
    while indexA < skipA:
        assert nodeA is not None
        nodeA = nodeA.next
        indexA += 1

    intersecting_node = nodeA

    indexB = 0
    nodeB = listB
    while indexB < skipB - 1:
        assert nodeB is not None
        nodeB = nodeB.next
        indexB += 1

    assert nodeB is not None
    nodeB.next = intersecting_node

    return listA, listB


def get_values(node: ListNode) -> list[int]:
    """Returns the values in linked list"""
    values = [node.val]
    curr = node.next
    while curr is not None:
        values.append(curr.val)
        curr = curr.next

    return values


def get_length(ll: Optional[ListNode]) -> int:
    """Returns length of linked list"""
    length = 0
    while ll is not None:
        ll = ll.next
        length += 1

    return length


class Solution:
    def getIntersectionNode(
            self,
            headA: Optional[ListNode],
            headB: Optional[ListNode],
    ) -> Optional[ListNode]:
        lenA = get_length(headA)
        lenB = get_length(headB)

        longer, shorter = (headA, headB) if lenA > lenB else (headB, headA)

        node1 = longer
        node2 = shorter
        for _ in range(abs(lenA - lenB)):
            assert node1 is not None
            node1 = node1.next

        while node1 is not None:
            assert node2 is not None

            if node1 == node2:
                return node1

            node1 = node1.next
            node2 = node2.next

        return None


tests = [
    (
        (8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3,),
        8,
    ),
    (
        (2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1,),
        2,
    ),
    (
        (0, [2, 6, 4], [1, 5], 3, 2,),
        None,
    ),
]


def validator(
        getIntersectionNode: Callable[
            [Optional[ListNode], Optional[ListNode]],
            Optional[ListNode]
        ],
        inputs: tuple[int, list[int], list[int], int, int],
        expected: int
) -> None:
    _, values1, values2, skipA, skipB = inputs
    node_list1, node_list2 = create_intersecting_lists(
        values1, values2, skipA, skipB,
    )
    intersecting_node = getIntersectionNode(node_list1, node_list2)
    node_value = intersecting_node.val if intersecting_node else None
    assert node_value == expected, (node_value, expected)
