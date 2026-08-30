class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = [(0,0)]
        ans = 0
        visited = set()
        while minHeap:
            dist, curr = heapq.heappop(minHeap)
            if curr in visited:
                continue
            ans += dist
            visited.add(curr)
            for dist, node in adj[curr]:
                if node in visited:
                    continue
                heapq.heappush(minHeap, (dist, node))
        return ans