class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lengths = []
        heapq.heapify(lengths)
        for point in points:
            x = point[0]
            y = point[1]
            dist = -math.sqrt(x**2 + y**2)
            heapq.heappush(lengths, (dist, [x,y]))
            if len(lengths) > k:
                heapq.heappop(lengths)
        res = []
        for _ in range(k):
            d, p = heapq.heappop(lengths)
            res.append(p)
        return res