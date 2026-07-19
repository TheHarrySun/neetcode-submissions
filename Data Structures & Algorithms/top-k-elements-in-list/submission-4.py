class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
        
        heap = []
        for key, val in counts.items():
            heap.append((-val, key))
        heapq.heapify(heap)
        
        res = []
        for _ in range(k):
            res.append(heap[0][1])
            heapq.heappop(heap)
        return res