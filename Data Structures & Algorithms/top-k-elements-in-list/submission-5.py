class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        hashmap = {}
        for entry in nums:
            hashmap[entry] = 1 + hashmap.get(entry, 0)
        for key,val in hashmap.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res