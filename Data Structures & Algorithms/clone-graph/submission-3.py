"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        if not node:
            return None

        new_input = Node(val = node.val)
        mapping[node] = [new_input, False]
        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            new_curr, visited = mapping[curr]
            if visited:
                continue
            for neighbor in curr.neighbors:
                if neighbor not in mapping:
                    new_neighbor = Node(neighbor.val)
                    mapping[neighbor] = [new_neighbor, False]
                new_curr.neighbors.append(mapping[neighbor][0])
                q.append(neighbor)
            mapping[curr][1] = True
        return new_input