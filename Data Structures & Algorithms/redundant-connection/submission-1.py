class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)

        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        for i, deg in enumerate(indegree):
            if deg == 1:
                q.append(i)
        
        while q:
            u = q.popleft()
            indegree[u] -= 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 1:
                    q.append(v)
        
        for i in range(len(edges) - 1, -1, -1):
            u = edges[i][0]
            v = edges[i][1]
            if indegree[u] == 2 and indegree[v] != 0:
                return edges[i]
        return []