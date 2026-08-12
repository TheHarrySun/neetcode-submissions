class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        q.append((0, -1))

        visited = set()
        while q:
            node, parent = q.popleft()
            visited.add(node)

            for i in adj[node]:
                if i == parent:
                    continue
                if i in visited:
                    return False
                q.append((i, node))
        return len(visited) == n