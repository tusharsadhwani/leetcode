from collections import deque
from typing import Optional

from testutils.graphs import GraphNode as Node, build_graph, get_adjacency_list


class Solution:
    def cloneGraph(self, root: 'Node') -> Optional['Node']:
        if root is None:
            return None

        root_copy = Node(val=root.val)
        # maps nodes to their copies
        copies = {root: root_copy}

        node_queue: deque[Node] = deque()
        node_queue.append(root)
        while node_queue:
            node = node_queue.popleft()

            for neighbor in node.neighbors:
                if neighbor in copies:
                    # This neighbour has already been processed
                    neighbor_copy = copies[neighbor]
                else:
                    # This neighbour has NOT already been processed.
                    # So, create and store neighbor_copy...
                    neighbor_copy = Node(neighbor.val)
                    copies[neighbor] = neighbor_copy
                    # ...and add this neighbor for processing.
                    node_queue.append(neighbor)

                # only make one sided edge, from node to neighbor
                copies[node].neighbors.append(neighbor_copy)

        root_copy = copies[root]
        return root_copy


tests = [
    (
        ([[2, 4], [1, 3], [2, 4], [1, 3]],),
        [[2, 4], [1, 3], [2, 4], [1, 3]]
    ),
    (
        ([[]],),
        [[]],
    ),
]


def validator(
    cloneGraph: list[list[int]],
    inputs: tuple[list[list[int]]],
    expected: list[list[int]],
) -> None:
    adjacency_list, = inputs
    root = build_graph(adjacency_list)

    output = get_adjacency_list(root)
    assert output == expected, (output, expected)
