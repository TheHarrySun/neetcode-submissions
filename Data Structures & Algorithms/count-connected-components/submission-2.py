class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def bfs(node):
            q = deque()
            q.append(node)
            visited.add(node)
            while q:
                curr = q.popleft()
                for entry in adj[curr]:
                    if entry not in visited:
                        q.append(entry)
                        visited.add(entry)
        
        res = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        return res