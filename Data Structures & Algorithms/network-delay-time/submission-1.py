class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))

        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        visited = set()
        time = 0
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
                continue
            visited.add(v1)
            time = t1
            for v2, t2 in edges[v1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (t2 + t1, v2))
        return time if len(visited) == n else -1