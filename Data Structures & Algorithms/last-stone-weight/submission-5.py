class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-val for val in stones]
        heapq.heapify(weights)
        while len(weights) > 1:
            x = -heapq.heappop(weights)
            y = -heapq.heappop(weights)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(weights, x - y)
            else:
                heapq.heappush(weights, y - x)
        return 0 if len(weights) == 0 else -weights[0]