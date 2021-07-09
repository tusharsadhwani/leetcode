from collections import deque
from typing import Optional


class GraphNode:
    def __init__(self, val: int, neighbors: Optional[list['GraphNode']] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f'GraphNode(val={self.val})'


def build_graph(adjacency_list: list[list[int]]) -> Optional[GraphNode]:
    if len(adjacency_list[0]) == 0:
        return None

    nodes: dict[int, GraphNode] = {}
    for node_value, neighbours in enumerate(adjacency_list, start=1):
        node = GraphNode(node_value)
        for neighbour_value in neighbours:
            if neighbour_value not in nodes:
                nodes[neighbour_value] = GraphNode(neighbour_value)

            neighbour = nodes[neighbour_value]

            node.neighbors.append(neighbour)
            neighbour.neighbors.append(node)

    return nodes[1]


def get_adjacency_list(root: Optional[GraphNode]) -> list[list[int]]:
    if root is None:
        return [[]]

    assert root.val == 1  # we're dealing with 1-indexed adjacency lists

    adjacency_list: list[list[int]] = []

    node_queue: deque[GraphNode] = deque()
    node_queue.append(root)
    # contains all nodes we've already processed
    processed = {root}

    while node_queue:
        node = node_queue.popleft()

        index = node.val - 1

        # extend the adjacency list dynamically
        while index >= len(adjacency_list):
            adjacency_list.append([])

        for neighbour in node.neighbors:
            adjacency_list[index].append(neighbour.val)

            if neighbour not in processed:
                node_queue.append(neighbour)
                processed.add(neighbour)

    return adjacency_list
